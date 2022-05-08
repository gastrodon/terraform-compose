from typing import Dict, List

from library.model.cli import ArgumentKind
from library.model.command.base import Command

ARGUMENTS_KV: List[str] = [
    "backend-config",
    "backend",
    "from-module",
    "get",
    "ignore-remote-version",
    "input",
    "lock-timeout",
    "lock",
    "lockfile",
    "plugin-dir",
]

ARGUMENTS_FLAG: List[str] = [
    "force-copy",
    "migrate-state",
    "no-color",
    "reconfigure",
    "upgrade",
]


class Init(Command):
    name = "init"

    @staticmethod
    def arguments() -> Dict[str, ArgumentKind]:
        return {
            **{it: ArgumentKind.kv for it in ARGUMENTS_KV},
            **{it: ArgumentKind.flag for it in ARGUMENTS_FLAG},
        }
