from typing import Dict, List, Optional

from library.types.item import Item

APPLY: Dict[str, Item] = {
    "input": Item(False, False, bool),
    "lock": Item(False, False, bool),
    "parallelism": Item(10, False, int),
    "path": Item(None, True, Optional[str]),
    "state-backup": Item(None, False, Optional[str]),
    "state-out": Item(None, False, Optional[str]),
    "state": Item(None, False, Optional[str]),
}

DESTROY: Dict[str, Item] = {
    **APPLY,
    "no-destroy": Item(False, False, bool),
}

PLAN: Dict[str, Item] = {
    "input": Item(False, False, bool),
    "path": Item(None, True, str),
    "refresh-only": Item(False, False, bool),
    "refresh": Item(False, False, bool),
    "replace": Item(None, False, Optional[str]),
    "target": Item(None, False, Optional[str]),
    "var-files": Item([], False, List[str]),
    "vars": Item(dict(), False, Dict[str, str]),
}

INIT: Dict[str, Item] = {
    "backend-config": Item([], False, List[str]),
    "backend": Item(True, False, bool),
    "force-copy": Item(False, False, bool),
    "get": Item(True, False, bool),
    "input": Item(False, False, bool),
    "migrate-state": Item(False, False, bool),
    "plugin-dir": Item([], False, List[str]),
    "reconfigure": Item(False, False, bool),
    "upgrade": Item(False, False, bool),
}
