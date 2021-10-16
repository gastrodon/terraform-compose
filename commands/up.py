from os import sys
from typing import Any, Dict, List

import typer
from typer import colors

import app
from library import terraform  # noqa
from library import config, depends
from library.types import options
from library.types.kind import Kind


def gather_plan(service: str, compose: Dict[str, Any]):
    return {
        "kind": Kind.plan,
        "args": [],
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


@app.app.command(name="up")
def handle_up(
    services: List[str] = options.services,
    file: str = options.file,
):
    compose = config.read_file(file)
    services = services or compose["services"].keys()

    order = [
        service
        for group in [
            depends.order(
                depends.tree(it, compose["services"]),
                compose["services"],
            )
            for it in services
        ]
        for service in group
    ]

    configs = {
        service: {
            "plan": gather_plan(service, compose),
            "apply": gather_apply(service, compose),
        }
        for service in order
    }

    for key, config_set in configs.items():
        for it in config_set.values():
            code, stdin, stdout = terraform.do(it["kind"], it["args"], it["kwargs"])

            if stdin:
                typer.secho(stdin, fg=colors.GREEN)

            if stdout:
                typer.secho(stdout, fg=colors.RED, err=True)

            if code != 0:
                typer.secho(f"terraform exited with code {code}, continue?")

                try:
                    if input().lower() != "y":
                        sys.exit(code)
                except KeyboardInterrupt:
                    sys.exit(code)
