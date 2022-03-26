import library.load.handle  # noqa
from library import resolve
from library.load.route import parse
from library.model import Compose, compose


def load(args: ..., name: str = "") -> Compose:
    return compose.from_dict(parse.parse(None, args, resolve.get(name)))
