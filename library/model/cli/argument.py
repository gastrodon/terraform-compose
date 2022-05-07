from dataclasses import dataclass
from typing import Any

from library.model.cli.scope import ArgumentScope
from library.model.command import Command
from library.model.command.kind import LOOKUP


@dataclass
class Argument:
    key: str
    value: Any
    scope: ArgumentScope


@dataclass
class ArgumentFlag:
    key: str
    scope: ArgumentScope
    value: Any = True


@dataclass
class ArgumentCommand:
    key: str
    value: Any = None

    @property
    def scope(self) -> ArgumentScope:
        return ArgumentScope.command.value(self.command)

    @property
    def command(self) -> Command:
        return LOOKUP[self.key]


@dataclass
class ArgumentSeparator:
    key: str = "--"
    value: Any = None
    scope: ArgumentScope = ArgumentScope.compose
