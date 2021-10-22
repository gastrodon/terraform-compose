from typing import Any, Dict

import yaml

from library.types.exceptions import ValidateFailed
from library.types.item import Item


def read_file(path: str):
    with open(path) as stream:
        return yaml.safe_load(stream)


def read(
    schema: Dict[str, Item], service: str, compose: Dict[str, any]
) -> Dict[str, Any]:
    values = {
        key: compose["services"][service].get(  # TODO validate compose structure
            key,
            schema[key].default,
        )
        for key, value in schema.items()
    }

    for key, value in values.items():
        if not schema[key].validate(value):
            ValidateFailed(
                service,
                key,
                schema[key].type,
                value,
            ).exit()

    return values
