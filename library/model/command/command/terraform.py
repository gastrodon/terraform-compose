from typing import List

from library.model.cli import ArgumentFlag
from library.model.command.base import Command

ARGUMENTS_FLAG: List[str] = ["chdir"]


class Terraform(Command):
    @staticmethod
    def arguments() -> List[str]:
        return {it: ArgumentFlag for it in ARGUMENTS_FLAG}
