from typing import Dict, List

from library.model.cli import Argument, ArgumentFlag
from library.model.command.base import Command

ARGUMENTS_PLAN_KV: List[str] = [
    "compact_warnings",
    "input",
    "lock_timeout",
    "lock",
    "out",
    "parallelism",
    "refresh",
    "replace",
    "state",
    "target",
    "var_file",
    "var",
]

ARGUMENTS_FLAG_FLAG: List[str] = [
    "detailed_exitcode",
    "refresh_only",
    "no_color",
]

ARGUMENTS_APPLY_KV: List[str] = [
    "backup",
    "input",
    "lock_timeout",
    "lock",
    "parallelism",
    "state_out",
    "state",
]

ARGUMENTS_APPLY_FLAG: List[str] = [
    "auto_approve",
    "compact_warnings",
    "no_color",
]


class Up(Command):
    @staticmethod
    def arguments() -> Dict[str, Argument]:
        return {
            **{it: Argument for it in ARGUMENTS_PLAN_KV + ARGUMENTS_APPLY_KV},
            **{it: ArgumentFlag for it in ARGUMENTS_PLAN_FLAG + ARGUMENTS_APPLY_FLAG},
        }


class Down(Up):
    ...
