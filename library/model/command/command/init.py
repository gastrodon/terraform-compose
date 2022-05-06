from typing import List

from library.model.command.base import Command

ARGUMENTS_FLAG: List[str] = [
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
    def arguments_flag() -> List[str]:
        return ARGUMENTS_FLAG

    @staticmethod
    def arguments_kv() -> List[str]:
        return ARGUMENTS_KV
