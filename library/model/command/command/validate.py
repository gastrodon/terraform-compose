from typing import Dict, List

from library.model.cli import Argument, ArgumentFlag
from library.model.command.base import Command

ARGUMENTS_FLAG: List[str] = ["json", "no_color"]


class Validate(Command):
    @staticmethod
    def arguments_flag() -> Dict[str, Argument]:
        return {it: ArgumentFlag for it in ARGUMENTS_FLAG}
