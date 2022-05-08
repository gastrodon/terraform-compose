from typing import List

import library.load.handle  # noqa
from library import resolve
from library.load.route import parse
from library.model import Compose, compose
from library.model.cli import Argument


def load(args: List[Argument], name: str = "") -> Compose:
    return compose.from_dict(parse.parse(args, resolve.get(name)))
