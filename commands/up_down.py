from os import sys
from typing import Any, Dict, List

import typer

import app
from library import config, depends, terraform
from library.types import options
from library.types.kind import Kind


def gather_services(services: List[str], compose: Dict[str, Any]) -> List[str]:
    trees = [depends.tree(service, compose["services"]) for service in services]
    ordered = [service for ordered in map(depends.order, trees) for service in ordered]

    return depends.uniqie(ordered)


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

    configs = {
        service: {
            "plan": gather_plan(service, compose, destroy=destroy),
            "apply": gather_apply(service, compose),
        }
        for service in gather_services(services, compose)[:: -1 if destroy else 1]
    }

    for name, config_set in configs.items():
        code, stdout, stderr = terraform.do_up(name, config_set)

        if code:
            if stderr:
                typer.secho(stderr, err=True)

            typer.secho(f"terraform exited with code {code}, continue?")

            try:
                if input().lower() != "y":
                    sys.exit(code)
            except KeyboardInterrupt:
                sys.exit(code)


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
