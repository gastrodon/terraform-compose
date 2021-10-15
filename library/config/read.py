from typing import Any, Dict

import yaml

from library.types.exceptions import ValidateFailed
from library.types.kind import Kind


def read_file(path: str):
    with open(path) as stream:
        return yaml.safe_load(stream)


def read(kind: Kind, service: str, service_config: Dict[str, Any]) -> Dict[str, Any]:
    schema = kind.schema

    values = {
        key: service_config.get(
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
