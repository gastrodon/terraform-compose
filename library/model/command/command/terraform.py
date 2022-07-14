from typing import Dict

from library import value
from library.cli import parse
from library.model.cli import ArgumentKind
from library.model.cli.parse import ArgumentParser
from library.model.command.base import Command


class Terraform(Command):
    name = "terraform"

    @staticmethod
    def arguments() -> Dict[str, ArgumentParser]:
        return {
            "file": ArgumentParser(ArgumentKind.kv, value.COMPOSE_FILE),
            "context": ArgumentParser(ArgumentKind.kv, value.CONTEXT),
            "service": ArgumentParser(ArgumentKind.kv, [], parser=parse.listy),
        }
