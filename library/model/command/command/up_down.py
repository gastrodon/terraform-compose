from typing import List

from library.model.command.base import Command

ARGUMENTS_PLAN_FLAG: List[str] = [
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

ARGUMENTS_FLAG_KV: List[str] = [
    "detailed_exitcode",
    "destroy",
    "refresh_only",
    "no_color",
]

ARGUMENTS_APPLY_FLAG: List[str] = [
    "backup",
    "input",
    "lock_timeout",
    "lock",
    "parallelism",
    "state_out",
    "state",
]

ARGUMENTS_APPLY_KV: List[str] = [
    "auto_approve",
    "compact_warnings",
    "no_color",
]


class Up(Command):
    @staticmethod
    def arguments_flag() -> List[str]:
        return [*{*ARGUMENTS_PLAN_FLAG, *ARGUMENTS_APPLY_FLAG}]

    @staticmethod
    def arguments_kv() -> List[str]:
        return [*{*ARGUMENTS_PLAN_KV, *ARGUMENTS_APPLY_KV}]


class Down(Up):
    ...
