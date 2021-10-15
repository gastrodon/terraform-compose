from typing import Any, Dict

from library.config.kind import Kind


def read(kind: Kind, service_config: Dict[str, Any]) -> Dict[str, Any]:
    schema = kind.schema

    values = {
        key: service_config.get(
            key,
            schema[key].default,
        )
        for key, value in schema.items()
    }

    return {key: value for key, value in values.items() if schema[key].validate(value)}
