from dataclasses import dataclass
from typing import Any

from library.model.cli.scope import ArgumentScope


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
    scope: ArgumentScope = ArgumentScope.command


@dataclass
class ArgumentSeparator:
    key: str = "--"
    value: Any = None
    scope: ArgumentScope = ArgumentScope.compose
