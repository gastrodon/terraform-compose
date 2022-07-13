from typing import Dict

from library import value
from library.cli import parse
from library.model.cli import ArgumentKind
from library.model.cli.parse import Parser
from library.model.command.base import Command


class Terraform(Command):
    name = "terraform"

    @staticmethod
    def arguments() -> Dict[str, Parser]:
        return {
            "file": Parser(ArgumentKind.kv, value.COMPOSE_FILE),
            "context": Parser(ArgumentKind.kv, value.CONTEXT),
            "service": Parser(ArgumentKind.kv, [], parser=parse.listy),
        }
