from typing import List

from library.model.command.base import Command

ARGUMENTS_FLAG: List[str] = ["json", "no_color"]


class Validate(Command):
    @staticmethod
    def arguments_flag() -> List[str]:
        return ARGUMENTS_FLAG
