from dataclasses import dataclass, field
from typing import Dict

import dacite

from library.model.compose.service import Service


@dataclass
class Compose:
    service: Dict[str, Service] = field(default_factory=dict)


def from_dict(compose: Dict) -> Compose:
    return dacite.from_dict(data=compose, data_class=Compose)
