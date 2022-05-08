from typing import Dict, List

from library.model.cli import ArgumentKind
from library.model.command.base import Command

ARGUMENTS_FLAG: List[str] = ["json", "no-color"]


class Validate(Command):
    name = "validate"

    @staticmethod
    def arguments_flag() -> Dict[str, ArgumentKind]:
        return {it: ArgumentKind.flag for it in ARGUMENTS_FLAG}
