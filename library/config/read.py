from typing import Any, Dict

from library.config.kind import Kind
from library.types.exceptions import ValidateFailed


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
