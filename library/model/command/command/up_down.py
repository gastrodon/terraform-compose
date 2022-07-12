from typing import Dict

from library.cli import parse
from library.model.cli import ArgumentKind
from library.model.cli.parse import Parser
from library.model.command.base import Command

ARGUMENTS_PLAN: Dict[str, Parser] = {
    "compact-warnings": Parser(ArgumentKind.kv),
    "input": Parser(ArgumentKind.kv),
    "lock-timeout": Parser(ArgumentKind.kv),
    "lock": Parser(ArgumentKind.kv),
    "out": Parser(ArgumentKind.kv),
    "parallelism": Parser(ArgumentKind.kv),
    "refresh": Parser(ArgumentKind.kv, parser=parse.listy),
    "replace": Parser(ArgumentKind.kv),
    "state": Parser(ArgumentKind.kv),
    "target": Parser(ArgumentKind.kv, parser=parse.listy),
    "var-file": Parser(ArgumentKind.kv, parser=parse.listy),
    "var": Parser(ArgumentKind.kv),
    "detailed_exitcode": Parser(ArgumentKind.flag, False),
    "refresh-only": Parser(ArgumentKind.flag, False),
    "no-color": Parser(ArgumentKind.flag, False),
}

ARGUMENTS_APPLY: Dict[str, Parser] = {
    "backup": Parser(ArgumentKind.kv),
    "input": Parser(ArgumentKind.kv),
    "lock-timeout": Parser(ArgumentKind.kv),
    "lock": Parser(ArgumentKind.kv),
    "parallelism": Parser(ArgumentKind.kv),
    "state-out": Parser(ArgumentKind.kv),
    "state": Parser(ArgumentKind.kv),
    "auto-approve": Parser(ArgumentKind.flag, False),
    "compact-warnings": Parser(ArgumentKind.flag, False),
    "no-color": Parser(ArgumentKind.flag, False),
}


class Up(Command):
    name = "up"

    @staticmethod
    def arguments() -> Dict[str, Parser]:
        return {**ARGUMENTS_PLAN, **ARGUMENTS_APPLY}


class Down(Up):
    name = "down"
