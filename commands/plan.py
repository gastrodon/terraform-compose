import json
from typing import List

import typer

import app
from library import config, depends
from library.types import options
from library.types.kind import Kind


@app.app.command(name="plan")
def handle_plan(
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
        service: config.read(Kind.plan, service, compose["services"][service])
        for service in order
    }

    typer.echo(order)
    typer.echo(json.dumps(configs))
