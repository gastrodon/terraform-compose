from dataclasses import dataclass, field
from typing import Dict

import dacite

from library.model.config import Config


@dataclass
class Compose:
    services: Dict[str, Config] = field(default_factory=dict)


def from_dict(compose: Dict) -> Compose:
    return dacite.from_dict(data=compose, data_class=Compose)
