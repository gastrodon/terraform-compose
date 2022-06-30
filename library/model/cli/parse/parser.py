from dataclasses import dataclass
from typing import Any, Callable

from library.model.cli.kind import ArgumentKind


@dataclass
class Parser:
    kind: ArgumentKind
    default: Any = None
    rename: str = None
    parser: Callable[[Any], Any] = lambda it: it

    def parse(self, data: Any):
        return self.default if data == None else self.parser(data)
