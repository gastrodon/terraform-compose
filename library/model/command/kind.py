from enum import Enum
from typing import Dict


class CommandKind(Enum):
    terraform: str = "terraform"
    down: str = "down"
    graph: str = "graph"
    init: str = "init"
    show: str = "show"
    up: str = "up"
    validate: str = "validate"


COMMAND_KIND_LOOKUP: Dict[str, CommandKind] = {
    "terraform": CommandKind.terraform,
    "down": CommandKind.down,
    "graph": CommandKind.graph,
    "init": CommandKind.init,
    "show": CommandKind.show,
    "up": CommandKind.up,
    "validate": CommandKind.validate,
}
