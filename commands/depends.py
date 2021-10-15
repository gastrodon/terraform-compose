from typing import List

import typer

import app
from library import config, depends
from library.types import options


@app.app.command(name="depends")
def handle_depends(
    file: str = options.file,
    services: List[str] = options.services,
):
    compose = config.read_file(file)
    services = services or compose["services"].keys()

    trees = [depends.tree(service, compose["services"]) for service in services]

    typer.echo("\n\n".join(map(depends.render_tree, trees)))

    ordered = [service for ordered in map(depends.order, trees) for service in ordered]

    typer.echo("\nservices should be brought up in the following order:")
    typer.echo("\n".join(depends.uniqie(ordered)))
