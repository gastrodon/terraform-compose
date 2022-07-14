from typing import Dict

from library.model.command.base import Command  # noqa
from library.model.command.command import (  # noqa
    Down,
    Graph,
    Init,
    Show,
    Terraform,
    Up,
    Validate,
)
from library.model.command.kind import CommandKind  # noqa

COMMAND_LOOKUP: Dict[str, Command] = {
    "terraform": Terraform,
    "down": Down,
    "graph": Graph,
    "init": Init,
    "show": Show,
    "up": Up,
    "validate": Validate,
}
