from typing import Any, Dict, List

import typer

import app
from library import config, depends
from library.types import options


def render_groups(trees: List[Dict[str, Any]]):
    return [f"[ {', '.join(it)} ]" for it in depends.order_levels(trees)]


def render_graph(trees: List[Dict[str, Any]]):
    ordered = depends.order_flat(trees)
    return [
        depends.render_tree(it)
        for it in sorted(trees, key=lambda it: -1 * ordered.index(it["name"]))
    ]


@app.app.command(name="depends")
def handle_depends(
    file: str = options.file,
    services: List[str] = options.services,
    graph: bool = False,
):
    compose = config.read_file(file)
    services = services or compose["services"].keys()

    trees = [
        depends.dependency_tree(service, compose["services"]) for service in services
    ]

    rendered = render_graph(trees) if graph else render_groups(trees)
    typer.echo("\n".join(rendered))
