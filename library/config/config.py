from typing import Any, Dict

from library.config.kind import Kind


def load(service: str, config: Dict[str, Any], kind: Kind) -> Dict[str, Any]:
    return {
        key: value
        for key, value in config[service].items()
        if key in kind.schema and kind.schema[key].validate(value)
    }
