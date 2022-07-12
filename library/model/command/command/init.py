from typing import Dict

from library.model.cli import ArgumentKind
from library.model.cli.parse import Parser
from library.model.command.base import Command

ARGUMENTS: Dict[str, Parser] = {
    "backend-config": Parser(ArgumentKind.kv),
    "backend": Parser(ArgumentKind.kv),
    "from-module": Parser(ArgumentKind.kv),
    "ignore-remote-version": Parser(ArgumentKind.kv),
    "input": Parser(ArgumentKind.kv),
    "lock-timeout": Parser(ArgumentKind.kv),
    "lock": Parser(ArgumentKind.kv),
    "lockfile": Parser(ArgumentKind.kv),
    "plugin-dir": Parser(ArgumentKind.kv),
    "force-copy": Parser(ArgumentKind.flag, False),
    "get": Parser(ArgumentKind.flag, False),
    "migrate-state": Parser(ArgumentKind.flag, False),
    "no-color": Parser(ArgumentKind.flag, False),
    "reconfigure": Parser(ArgumentKind.flag, False),
    "upgrade": Parser(ArgumentKind.flag, False),
}


class Init(Command):
    name = "init"

    @staticmethod
    def arguments() -> Dict[str, Parser]:
        return ARGUMENTS
