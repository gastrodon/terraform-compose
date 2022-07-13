from dataclasses import dataclass, field
from typing import Dict

import dacite

from library.model.compose.service import Service


@dataclass
class Compose:
    service: Dict[str, Service] = field(default_factory=dict)


def be_snake(service: Dict) -> Dict:
    return {key.replace("-", "_"): value for key, value in service.items()}


def from_dict(compose: Dict) -> Compose:
    mapped = {
        "service": {
            name: be_snake(service) for name, service in compose["service"].items()
        }
    }

    return dacite.from_dict(data=mapped, data_class=Compose)
