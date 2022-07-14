from typing import Dict

from library.model.cli import ArgumentKind
from library.model.cli.parse import ArgumentParser
from library.model.command.base import Command


class Graph(Command):
    name = "graph"

    @staticmethod
    def arguments() -> Dict[str, ArgumentParser]:
        return {
            "groups": ArgumentParser(ArgumentKind.flag, False),
            "no-color": ArgumentParser(ArgumentKind.flag, False),
            "json": ArgumentParser(ArgumentKind.flag, False),
        }
