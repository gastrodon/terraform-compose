import os
from typing import Any, Dict

import yaml

from library.model import compose
from library.value import COMPOSE_FILE

lookup: Dict[str, Any] = {}


def path_to(name: str, file: str = COMPOSE_FILE) -> str:
    return os.path.abspath(
        os.path.join(
            *name.split("."),
            COMPOSE_FILE,
        )
    )


def gather(name: str = "", file: str = COMPOSE_FILE):
    global lookup

    if lookup.get(name):
        return

    with open(path_to(name, file)) as stream:
        lookup[name] = yaml.safe_load(stream)

    for imported in lookup[name].get("import", []):
        gather(".".join((name, imported)) if name else imported, file)


def set(composes: Dict[str, Dict]):
    global lookup

    lookup = {**composes}


def get(name: str):
    global lookup

    return lookup[name]


def get_compose(name: str):
    return compose.from_dict(get(name))
