from typing import Any, Dict, List

import typer

import app
from library.types import options
from library.types.item import Item
from library.types.kind import Kind

KIND_NAMES: Dict[str, Kind] = {kind.name: kind for kind in Kind}


def render_item(name: str, value: Item) -> str:
    return "\n\t\t".join(
        [
            f"{name}: {value.type}",
            f"required: {value.required}",
            f"default: {value.default}",
        ]
    )


def render_schema(action: Kind, schema: Dict[str, Any]) -> str:
    return "\n\t".join(
        [f"{action.name}:"]
        + [render_item(name, value) for name, value in schema.items()]
    )


@app.app.command(name="docs")
def handle_docs(
    actions: List[str] = options.actions,
    file: str = options.file,
    upgrade: bool = options.upgrade,
):
    """
    Draw docs for action schemas
    """
    rendered = [
        render_schema(kind, kind.schema)
        for kind in map(lambda it: KIND_NAMES[it], actions)
    ]

    typer.echo("\n\n".join(rendered))
