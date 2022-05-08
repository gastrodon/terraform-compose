from typing import Dict, List

from library.model.cli import ArgumentKind
from library.model.command.base import Command

ARGUMENTS_FLAG: List[str] = ["no-color", "json"]


class Show(Command):
    name = "show"

    @staticmethod
    def arguments() -> Dict[str, ArgumentKind]:
        return {it: ArgumentKind.flag for it in ARGUMENTS_FLAG}
