import os

import yaml

import library.load.handle  # noqa
from library.load.route import parse
from library.model import Compose, compose
from library.value import COMPOSE_FILE


def load(args: ..., path: str = ".", file: str = COMPOSE_FILE) -> Compose:
    # TODO better path / file exists / is valid checking

    with open(os.path.join(path, file)) as stream:
        parsed = parse.parse(None, args, yaml.safe_load(stream.read()))

    return compose.from_dict(parsed)
