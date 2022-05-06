from enum import Enum

from library.model.cli.argument import Argument, ArgumentCommand, ArgumentSeparator


class ArgumentKind(Enum):
    argument: Argument = Argument
    command: Argument = ArgumentCommand
    separator: Argument = ArgumentSeparator
