from typing import List

from library.model.command.base import Command

ARGUMENTS_PLAN: List[str] = [
    "compact_warnings",
    "destroy",
    "detailed_exitcode",
    "input",
    "lock_timeout",
    "lock",
    "no_color",
    "out",
    "parallelism",
    "refresh_only",
    "refresh",
    "replace",
    "state",
    "target",
    "var_file",
    "var",
]

ARGUMENTS_APPLY: List[str] = [
    "auto_approve",
    "backup",
    "compact_warnings",
    "input",
    "lock_timeout",
    "lock",
    "no_color",
    "parallelism",
    "state_out",
    "state",
]


class Up(Command):
    @staticmethod
    def arguments() -> List[str]:
        return [*{*ARGUMENTS_PLAN, *ARGUMENTS_APPLY}]


class Down(Up):
    ...
