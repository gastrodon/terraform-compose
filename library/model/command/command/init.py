from typing import Dict, List

from library.model.cli import Argument, ArgumentFlag
from library.model.command.base import Command

ARGUMENTS_KV: List[str] = [
    "backend_config",
    "backend",
    "from_module",
    "get",
    "ignore_remote_version",
    "input",
    "lock_timeout",
    "lock",
    "lockfile",
    "plugin_dir",
]

ARGUMENTS_FLAG: List[str] = [
    "force_copy",
    "migrate_state",
    "no_color",
    "reconfigure",
    "upgrade",
]


class Init(Command):
    @staticmethod
    def arguments() -> Dict[str, Argument]:
        return {
            **{it: Argument for it in ARGUMENTS_KV},
            **{it: ArgumentFlag for it in ARGUMENTS_FLAG},
        }
