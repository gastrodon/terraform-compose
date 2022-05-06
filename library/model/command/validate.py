from typing import List

from library.model.command.command import Command

ARGUMENTS: List[str] = ["json", "no_color"]


class Validate(Command):
    @staticmethod
    def arguments() -> List[str]:
        return ARGUMENTS
