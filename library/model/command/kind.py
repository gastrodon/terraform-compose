from enum import Enum
from typing import Dict

from library.model.command import command
from library.model.command.base import Command


class CommandKind(Enum):
    down: Command = command.Down
    graph: Command = command.Graph
    init: Command = command.Init
    show: Command = command.Show
    up: Command = command.Up
    validate: Command = command.Validate


LOOKUP: Dict[str, CommandKind] = {
    "down": CommandKind.down,
    "graph": CommandKind.graph,
    "init": CommandKind.init,
    "show": CommandKind.show,
    "up": CommandKind.up,
    "validate": CommandKind.validate,
}
