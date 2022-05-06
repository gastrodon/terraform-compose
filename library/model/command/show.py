from typing import List

from library.model.command.command import Command

ARGUMENTS: List[str] = ["no_color", "json"]


class Show(Command):
    @staticmethod
    def arguments() -> List[str]:
        return ARGUMENTS
