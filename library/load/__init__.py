from typing import List

import library.load.handle  # noqa
from library import resolve
from library.load.route import parse
from library.model.cli import Argument
from library.model.compose import Compose


def load(name: str, args: List[Argument]) -> Compose:
    return Compose(service=parse.parse(args, resolve.get(name))["service"])
