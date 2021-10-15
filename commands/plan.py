import json
from typing import List

import typer

import app
from library import depends, load
from library.config import Kind
from library.types import options


@app.app.command(name="plan")
def handle_plan(
    services: List[str] = options.services,
    file: str = options.file,
):
    config = load.from_name(file)
    services = services or config["services"].keys()

    order = [
        service
        for group in [
            depends.order(
                depends.tree(it, config["services"]),
                config["services"],
            )
            for it in services
        ]
        for service in group
    ]

    configs = {
        service: config.read(Kind.plan, config["services"][service])
        for service in order
    }

    typer.echo(order)
    typer.echo(json.dumps(configs))
