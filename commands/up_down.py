from multiprocessing import Pool
from typing import Any, Dict, List

import typer

import app
from library import config, depends, terraform
from library.types import options
from library.types.kind import Kind


def gather_services(services: List[str], compose: Dict[str, Any]) -> List[List[str]]:
    return depends.order_levels(
        [depends.dependency_tree(service, compose["services"]) for service in services]
    )


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


def thread_plan_apply(config: Dict[str, Any]):
    for action_config in config.values():
        code, stdout, stderr = terraform.do(
            action_config["kind"],
            action_config["args"],
            action_config["kwargs"],
        )

        if stdout and code != 0:
            typer.secho(stdout)

        if stderr and code != 0:
            typer.secho(stderr, err=True)

        if code != 0:
            raise Exception(f"terraform exited with code {code}")


def do_cluster(configs: List[Dict[str, Any]]) -> List[Any]:
    with Pool(processes=len(configs)) as pool:
        return pool.map(thread_plan_apply, configs.values())


def do_plan_apply(
    services: List[str] = options.services,
    file: str = options.file,
    destroy: bool = False,
):
    compose = config.read_file(file)
    services = services or compose["services"].keys()

    config_groups: List[Dict[str, Any]] = [
        {
            service: {
                "plan": gather_plan(service, compose, destroy=destroy),
                "apply": gather_apply(service, compose),
            }
            for service in cluster
        }
        for cluster in gather_services(services, compose)[:: -1 if destroy else 1]
    ]

    for group in config_groups:
        with Pool(processes=len(group)) as pool:
            pool.map(thread_plan_apply, group.values())


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
