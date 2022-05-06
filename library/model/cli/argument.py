from dataclasses import dataclass
from typing import Any

from library.model.command import Command
from library.model.command.kind import LOOKUP


@dataclass
class Argument:
    key: str
    value: Any


@dataclass
class ArgumentFlag:
    key: str
    value: Any = True


@dataclass
class ArgumentCommand:
    key: str
    value: Any = None

    @property
    def command(self) -> Command:
        return LOOKUP[self.key]


@dataclass
class ArgumentSeparator:
    key: str = "--"
    value: Any = None
