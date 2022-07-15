import os
from typing import Any, Dict

import yaml

from library.value import COMPOSE_FILE

lookup: Dict[str, Any] = {}


def path_to(name: str, context: str, file: str) -> str:
    return os.path.abspath(
        os.path.join(
            context,
            *name.split("."),
            COMPOSE_FILE,
        )
    )


def gather(name: str = "", context: str = ".", file: str = COMPOSE_FILE):
    global lookup

    if lookup.get(name):
        return

    with open(path_to(name, context, file)) as stream:
        lookup[name] = yaml.safe_load(stream)

    for imported in lookup[name].get("import", []):
        gather(".".join((name, imported)) if name else imported, context, file)


def set(composes: Dict[str, Dict]):
    global lookup

    lookup = {**composes}


def get(name: str):
    global lookup

    return lookup[name]
