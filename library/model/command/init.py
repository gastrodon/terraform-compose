from typing import List

from library.model.command.command import Command

ARGUMENTS: List[str] = [
    "backend_config",
    "backend",
    "force_copy",
    "from_module",
    "get",
    "ignore_remote_version",
    "input",
    "lock_timeout",
    "lock",
    "lockfile",
    "migrate_state",
    "no_color",
    "plugin_dir",
    "reconfigure",
    "upgrade",
]


class Init(Command):
    @staticmethod
    def arguments() -> List[str]:
        return ARGUMENTS
