from multiprocessing import Pool
from typing import Any, Callable, Dict, List

import typer

import app
from library import config, depends, terraform
from library.types import options
from library.types.kind import Kind


def gather_services(
    services: List[str], compose: Dict[str, Any], destroy: False
) -> List[List[str]]:
    if destroy:
        skip: Callable[[Dict[str, Any]], bool] = lambda it: it.get("no-destroy")
    else:
        skip: Callable[[Dict[str, Any]], bool] = lambda it: False

    trees: List[Dict[str, Any]] = [
        depends.dependency_tree(service, compose["services"], skip=skip)
        for service in services
    ]

    return depends.order_levels(trees)[:: -1 if destroy else 1]


def gather_plan(service: str, compose: Dict[str, Any], destroy: bool = False):
    return {
        "kind": Kind.plan,
        "args": ["--destroy"] if destroy else [],
        "kwargs": {
            **config.read(Kind.plan, service, compose["services"][service]),
            "out": "terraform-compose-tfplan",
        },
    }


def gather_apply(service: str, compose: Dict[str, Any]):
    return {
        "kind": Kind.apply,
        "args": ["terraform-compose-tfplan"],
        "kwargs": {
            **config.read(Kind.apply, service, compose["services"][service]),
        },
    }


def do_plan_apply(
    services: List[str] = options.services,
    file: str = options.file,
    destroy: bool = False,
):
    compose = config.read_file(file)
    services = services or compose["services"].keys()

    config_groups: List[List[Dict[str, Any]]] = [
        [
            {
                "service": service,
                "plan": gather_plan(service, compose, destroy=destroy),
                "apply": gather_apply(service, compose),
            }
            for service in cluster
        ]
        for cluster in gather_services(services, compose, destroy)
    ]

    if not config_groups:
        typer.echo("nothing to do")

    for group in config_groups:
        with Pool(processes=len(group)) as pool:
            pool.map(terraform.do_up, group)


@app.app.command(name="up")
def handle_up(
    services: List[str] = options.services,
    file: str = options.file,
):
    do_plan_apply(services, file, destroy=False)


@app.app.command(name="down")
def handle_down(
    services: List[str] = options.services,
    file: str = options.file,
):
    do_plan_apply(services, file, destroy=True)
