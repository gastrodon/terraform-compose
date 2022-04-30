from enum import Enum

from library.model import Command, command


class CommandKind(Enum):
    down: Command = command.Down
    graph: Command = command.Graph
    init: Command = command.Init
    refresh: Command = command.Refresh
    show: Command = command.Show
    up: Command = command.Up
    validate: Command = command.Validate
