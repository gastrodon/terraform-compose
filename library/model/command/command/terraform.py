from typing import Dict, List

from library.model.cli import ArgumentKind
from library.model.command.base import Command

ARGUMENTS_KV: List[str] = ["compose"]


class Terraform(Command):
    name = "terraform"

    @staticmethod
    def arguments() -> Dict[str, ArgumentKind]:
        return {it: ArgumentKind.kv for it in ARGUMENTS_KV}
