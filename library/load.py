from typing import Any

import yaml


def from_name(name: str) -> dict[str, Any]:
    with open(name) as stream:
        return yaml.safe_load(stream)
