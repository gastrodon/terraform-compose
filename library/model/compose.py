from dataclasses import dataclass, field
from typing import Dict

import dacite

from library.model.config import Config


@dataclass
class Compose:
    services: Dict[str, Config] = field(default_factory=dict)


def from_file(path: str) -> Compose:
    with open(path) as stream:
        return from_raw(path.read())


def from_raw(compose: str) -> Compose:
    return from_dict(yaml.safe_load(compose))


def from_dict(compose: Dict) -> Compose:
    return dacite.from_dict(data=compose, data_class=Compose)
