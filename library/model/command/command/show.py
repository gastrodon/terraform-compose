from typing import Dict, List

from library.model.cli import Argument, ArgumentFlag
from library.model.command.base import Command

ARGUMENTS_FLAG: List[str] = ["no_color", "json"]


class Show(Command):
    @staticmethod
    def arguments() -> Dict[str, Argument]:
        return {it: ArgumentFlag for it in ARGUMENTS_FLAG}
