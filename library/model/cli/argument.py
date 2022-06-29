from dataclasses import dataclass
from typing import Any

from library.model.cli.kind import ArgumentKind
from library.model.cli.scope import ArgumentScope


@dataclass
class Argument:
    ...


@dataclass
class ArgumentKV(Argument):
    key: str
    value: Any
    scope: ArgumentScope
    kind: ArgumentKind = ArgumentKind.kv


@dataclass
class ArgumentFlag(Argument):
    key: str
    scope: ArgumentScope
    value: Any = True
    kind: ArgumentKind = ArgumentKind.flag


@dataclass
class ArgumentCommand(Argument):
    key: str
    value: Any = None
    scope: ArgumentScope = ArgumentScope.command
    kind: ArgumentKind = ArgumentKind.command


@dataclass
class ArgumentSeparator(Argument):
    key: str = "--"
    value: Any = None
    scope: ArgumentScope = ArgumentScope.compose
    kind: ArgumentKind = ArgumentKind.separator
