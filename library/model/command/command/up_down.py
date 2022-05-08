from typing import Dict, List

from library.model.cli import ArgumentKind
from library.model.command.base import Command

ARGUMENTS_PLAN_KV: List[str] = [
    "compact-warnings",
    "input",
    "lock-timeout",
    "lock",
    "out",
    "parallelism",
    "refresh",
    "replace",
    "state",
    "target",
    "var-file",
    "var",
]

ARGUMENTS_PLAN_FLAG: List[str] = [
    "detailed_exitcode",
    "refresh-only",
    "no-color",
]

ARGUMENTS_APPLY_KV: List[str] = [
    "backup",
    "input",
    "lock-timeout",
    "lock",
    "parallelism",
    "state-out",
    "state",
]

ARGUMENTS_APPLY_FLAG: List[str] = [
    "auto-approve",
    "compact-warnings",
    "no-color",
]


class Up(Command):
    name = "up"

    @staticmethod
    def arguments() -> Dict[str, ArgumentKind]:
        return {
            **{it: ArgumentKind.kv for it in ARGUMENTS_PLAN_KV + ARGUMENTS_APPLY_KV},
            **{
                it: ArgumentKind.flag
                for it in ARGUMENTS_PLAN_FLAG + ARGUMENTS_APPLY_FLAG
            },
        }


class Down(Up):
    name = "down"
