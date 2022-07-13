from typing import List

import library.load.handle  # noqa
from library import resolve
from library.load.route import parse
from library.model.cli import Argument
from library.model.compose import Compose, compose


def load(args: List[Argument], name: str = "") -> Compose:
    return compose.from_dict(parse.parse(args, resolve.get(name)))
