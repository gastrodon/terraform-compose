from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Compose:
    service: Dict[str, Dict] = field(default_factory=dict)
