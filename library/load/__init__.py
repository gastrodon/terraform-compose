import yaml

import library.load.handle  # noqa
from library.load.route import parse
from library.model import Compose, compose

PATH_COMPOSE = "./terraform-compose.yml"


def load(args: ..., path: str = PATH_COMPOSE) -> Compose:
    with open(path) as stream:
        parsed = parse.parse(None, args, yaml.safe_load(stream.read()))

    return compose.from_dict(parsed)
