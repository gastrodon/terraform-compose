from typing import Dict

from library.model.cli import ArgumentKind
from library.model.cli.parse import ArgumentParser
from library.model.command.base import Command


class Show(Command):
    name = "show"

    @staticmethod
    def arguments() -> Dict[str, ArgumentParser]:
        return {
            "no-color": ArgumentParser(ArgumentKind.flag, False),
            "json": ArgumentParser(ArgumentKind.flag, False),
        }
