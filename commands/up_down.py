from multiprocessing import Pool
from typing import Any, Callable, Dict, List

import typer

import app
from library import config, depends, terraform
from library.config.defaults import APPLY, PLAN
from library.types import options
from library.types.kind import Kind


def gather_services(
    services: List[str],
    compose: Dict[str, Any],
    destroy: False,
) -> List[List[str]]:
    if destroy:
        skip: Callable[[Dict[str, Any]], bool] = lambda it: it.get("no-destroy")
    else:
        skip: Callable[[Dict[str, Any]], bool] = lambda it: False

    root = depends.root_dependency_tree(compose["services"], skip=skip, inverse=destroy)
    trees = [*filter(bool, [depends.pluck(service, root) for service in services])]
    return depends.order_levels(trees)[:: -1 if destroy else 1]


def gather_plan(
    service: str,
    compose: Dict[str, Any],
    destroy: bool = False,
) -> Dict[str, Any]:
    return {
        "kind": Kind.plan,
        "args": ["-json", "-destroy"] if destroy else ["-json"],
        "kwargs": {
            **config.read(PLAN, service, compose),
            "out": "terraform-compose-tfplan",
        },
    }


def gather_apply(service: str, compose: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "kind": Kind.apply,
        "args": ["-json", "terraform-compose-tfplan"],
        "kwargs": {
            **config.read(APPLY, service, compose),
        },
    }


def do_plan_apply(
    services: List[str] = options.services,
    file: str = options.file,
    destroy: bool = False,
):
    compose: Dict[str, Any] = config.read_file(file)
    services: List[str] = services or compose["services"].keys()

    config_groups: List[List[Dict[str, Any]]] = [
        [
            {
                "service": service,
                "destroy": destroy,
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
    """
    Bring up selected services and their dependencies
    """
    do_plan_apply(services, file, destroy=False)


@app.app.command(name="down")
def handle_down(
    services: List[str] = options.services,
    file: str = options.file,
):
    """
    Bring down selected services and their dependants
    """
    # TODO docs are wrong
    do_plan_apply(services, file, destroy=True)
