from enum import Enum

from library.model.command.kind import CommandKind


class ArgumentScope(Enum):
    terraform = "terraform"
    command = CommandKind
    compose = "compose"
