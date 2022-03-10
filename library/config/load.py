from typing import Dict, List

from library.config import middleware
from library.types.config import Config


def from_file(args: List, file: str) -> Dict[str, Config]:
    with open(file) as stream:
        return from_raw(args, stream.read())


def from_raw(args: List, config: str) -> Dict[str, Config]:
    return middleware.parser.raw(args, config)
