from typing import Dict

from library.cli import parse
from library.model.cli import ArgumentKind
from library.model.cli.parse import ArgumentParser
from library.model.command.base import Command

ARGUMENTS_PLAN: Dict[str, ArgumentParser] = {
    "compact-warnings": ArgumentParser(ArgumentKind.kv),
    "input": ArgumentParser(ArgumentKind.kv),
    "lock-timeout": ArgumentParser(ArgumentKind.kv),
    "lock": ArgumentParser(ArgumentKind.kv),
    "out": ArgumentParser(ArgumentKind.kv),
    "parallelism": ArgumentParser(ArgumentKind.kv),
    "refresh": ArgumentParser(ArgumentKind.kv, parser=parse.listy),
    "replace": ArgumentParser(ArgumentKind.kv),
    "state": ArgumentParser(ArgumentKind.kv),
    "target": ArgumentParser(ArgumentKind.kv, parser=parse.listy),
    "var-file": ArgumentParser(ArgumentKind.kv, parser=parse.listy),
    "var": ArgumentParser(ArgumentKind.kv, parser=parse.dicty),
    "detailed_exitcode": ArgumentParser(ArgumentKind.flag, False),
    "refresh-only": ArgumentParser(ArgumentKind.flag, False),
    "no-color": ArgumentParser(ArgumentKind.flag, False),
}

ARGUMENTS_APPLY: Dict[str, ArgumentParser] = {
    "backup": ArgumentParser(ArgumentKind.kv),
    "input": ArgumentParser(ArgumentKind.kv),
    "lock-timeout": ArgumentParser(ArgumentKind.kv),
    "lock": ArgumentParser(ArgumentKind.kv),
    "parallelism": ArgumentParser(ArgumentKind.kv),
    "state-out": ArgumentParser(ArgumentKind.kv),
    "state": ArgumentParser(ArgumentKind.kv),
    "auto-approve": ArgumentParser(ArgumentKind.flag, False),
    "compact-warnings": ArgumentParser(ArgumentKind.flag, False),
    "no-color": ArgumentParser(ArgumentKind.flag, False),
}


class Up(Command):
    name = "up"

    @staticmethod
    def arguments() -> Dict[str, ArgumentParser]:
        return {**ARGUMENTS_PLAN, **ARGUMENTS_APPLY}


class Down(Up):
    name = "down"
