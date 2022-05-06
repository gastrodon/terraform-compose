from enum import Enum

from library.model.command.kind import CommandKind


class ArgumentScope(Enum):
    terraform: str
    command: CommandKind
    compose: str
