from typing import Dict

from library.model.cli import ArgumentKind
from library.model.cli.parse import Parser
from library.model.command.base import Command


class Validate(Command):
    name = "validate"

    @staticmethod
    def arguments() -> Dict[str, Parser]:
        return {
            "no-color": Parser(ArgumentKind.flag, False),
            "json": Parser(ArgumentKind.flag, False),
        }
