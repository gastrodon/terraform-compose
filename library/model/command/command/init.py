from typing import Dict

from library.model.cli import ArgumentKind
from library.model.cli.parse import ArgumentParser
from library.model.command.base import Command

ARGUMENTS: Dict[str, ArgumentParser] = {
    "backend-config": ArgumentParser(ArgumentKind.kv),
    "backend": ArgumentParser(ArgumentKind.kv),
    "from-module": ArgumentParser(ArgumentKind.kv),
    "ignore-remote-version": ArgumentParser(ArgumentKind.kv),
    "input": ArgumentParser(ArgumentKind.kv),
    "lock-timeout": ArgumentParser(ArgumentKind.kv),
    "lock": ArgumentParser(ArgumentKind.kv),
    "lockfile": ArgumentParser(ArgumentKind.kv),
    "plugin-dir": ArgumentParser(ArgumentKind.kv),
    "force-copy": ArgumentParser(ArgumentKind.flag, False),
    "get": ArgumentParser(ArgumentKind.flag, False),
    "migrate-state": ArgumentParser(ArgumentKind.flag, False),
    "no-color": ArgumentParser(ArgumentKind.flag, False),
    "reconfigure": ArgumentParser(ArgumentKind.flag, False),
    "upgrade": ArgumentParser(ArgumentKind.flag, False),
}


class Init(Command):
    name = "init"

    @staticmethod
    def arguments() -> Dict[str, ArgumentParser]:
        return ARGUMENTS
