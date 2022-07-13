from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Service:
    path: str = "."
    no_destroy: bool = False

    input: bool = False
    lock: bool = False
    parallelism: int = 10
    state: Optional[str] = None
    state_backup: Optional[str] = None
    state_out: Optional[str] = None

    refresh: bool = False
    refresh_only: bool = None
    replace: List[str] = field(default_factory=list)
    target: List[str] = field(default_factory=list)
    var: Dict[str, Any] = field(default_factory=dict)
    var_file: List[str] = field(default_factory=list)

    migrate_state: bool = False
    reconfigure: bool = False
    get_modules: bool = True
    lock: bool = True
    input: bool = False
    backend: bool = True
    backend_config: List[str] = field(default_factory=list)
