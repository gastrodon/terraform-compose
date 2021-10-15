from typing import Dict, List, Optional

from library.types.item import Item

APPLY: Dict[str, Item] = {
    "auto-approve": Item(False, False, bool),
    "compact-warnings": Item(False, False, bool),
    "lock": Item(False, False, bool),
    "no-color": Item(False, False, bool),
    "parallelism": Item(10, False, int),
    "path": Item(None, True, str),
    "state-backup": Item(None, False, str),
    "state-out": Item(None, False, str),
    "state": Item(None, False, str),
}

DESTROY: Dict[str, Item] = {**APPLY}

PLAN: Dict[str, Item] = {
    "path": Item(None, True, str),
    "refresh-only": Item(False, False, bool),
    "refresh": Item(False, False, bool),
    "replace": Item(None, False, Optional[str]),
    "target": Item(None, False, Optional[str]),
    "var-files": Item([], False, List[str]),
    "vars": Item({}, False, Dict[str, str]),
}
