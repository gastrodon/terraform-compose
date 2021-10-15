import json
from typing import List

import typer

import app
from library import config, depends, load
from library.config import Kind
from library.types import options


@app.app.command(name="plan")
def handle_plan(
    services: List[str] = options.services,
    file: str = options.file,
):
    compose = load.from_name(file)
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
