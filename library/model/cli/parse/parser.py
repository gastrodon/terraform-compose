from dataclasses import dataclass, field
from typing import Any, Callable, Set

from library.model.cli.kind import ArgumentKind
from library.model.terraform import TerraformCommand


@dataclass
class ArgumentParser:
    kind: ArgumentKind
    default: Any = None
    rename: str = None
    commands: Set[TerraformCommand] = field(default_factory=set)
    parser: Callable[[Any], Any] = lambda it: it

    def parse(self, data: Any):
        return self.default if data == None else self.parser(data)
