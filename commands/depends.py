from typing import Any, Dict, List

import typer

import app
from library import config, depends
from library.types import options


def render_groups(trees: List[Dict[str, Any]]) -> List[str]:
    return [f"[ {', '.join(it)} ]" for it in depends.order_levels(trees)]


def render_graph(trees: List[Dict[str, Any]]) -> List[str]:
    ordered: List[Dict[str, Any]] = depends.order_flat(trees)
    return [
        depends.render_tree(it)
        for it in sorted(trees, key=lambda it: -1 * ordered.index(it["name"]))
    ]


@app.app.command(name="depends")
def handle_depends(
    file: str = options.file,
    services: List[str] = options.services,
    graph: bool = options.graph,
):
    """
    Show dependency graphs for selected services
    and the order by which services should be brought up
    """
    compose: Dict[str, Any] = config.read_file(file)
    services: List[str] = services or compose["services"].keys()

    trees: Dict[str, Any] = [
        depends.dependency_tree(service, compose["services"]) for service in services
    ]

    rendered: List[str] = render_graph(trees) if graph else render_groups(trees)
    typer.echo("\n".join(rendered))
