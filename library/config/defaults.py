from typing import Any, Dict, List


class Item:
    def __init__(self, default: Any, required: bool, type: Any):
        self.default = default
        self.required = required
        self.type = type


APPLY: Dict[str, Item] = {
    "auto-approve": Item(False, False, bool),
    "color": Item(True, False, bool),
    "compact-warnings": Item(False, False, bool),
    "lock": Item(False, False, bool),
    "state-backup": Item(None, False, str),
    "state-out": Item(None, False, str),
    "state-path": Item(None, False, str),
    "parallelism": Item(10, False, int),
}

DESTROY: Dict[str, Item] = {**APPLY}

PLAN: Dict[str, Item] = {
    "refresh-only": Item(False, False, bool),
    "refresh": Item(False, False, bool),
    "replace": Item(None, False, str),
    "target": Item(None, False, str),
    "var-files": Item([], False, List[str]),
    "vars": Item({}, False, [Dict[str, str]]),
}
