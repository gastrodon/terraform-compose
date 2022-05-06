from typing import List

from library.model.command.base import Command

ARGUMENTS_FLAG: List[str] = ["no_color", "json"]


class Show(Command):
    @staticmethod
    def arguments_flag() -> List[str]:
        return ARGUMENTS_FLAG
