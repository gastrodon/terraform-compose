from dataclasses import dataclass
from typing import Any

from library.model.cli.scope import ArgumentScope


@dataclass
class Argument:
    ...


@dataclass
class ArgumentKV(Argument):
    key: str
    value: Any
    scope: ArgumentScope


@dataclass
class ArgumentFlag(Argument):
    key: str
    scope: ArgumentScope
    value: Any = True


@dataclass
class ArgumentCommand(Argument):
    key: str
    value: Any = None
    scope: ArgumentScope = ArgumentScope.command


@dataclass
class ArgumentSeparator(Argument):
    key: str = "--"
    value: Any = None
    scope: ArgumentScope = ArgumentScope.compose
