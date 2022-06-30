from typing import Dict

from library.model.cli import ArgumentKind
from library.model.cli.parse import Parser
from library.model.command.base import Command


class Graph(Command):
    name = "graph"

    @staticmethod
    def arguments() -> Dict[str, Parser]:
        return {
            "groups": Parser(ArgumentKind.flag, False),
            "no-color": Parser(ArgumentKind.flag, False),
            "json": Parser(ArgumentKind.flag, False),
        }
