import os
from typing import Any, Dict, List

PATH_KEYS: List[str] = [
    "state-backup",
    "state-out",
    "state",
]

SKIP_KEYS: List[str] = ["backend-configs", "plan", "path", "var-files", "vars"]

FILE_COLLECTION_KEYS: Dict[str, str] = {
    "backend-configs": "backend-config",
    "var-files": "var-file",
}


def sanitize_config(config: Dict[str, Any]) -> Dict[str, Any]:
    return {key: value for key, value in {**config}.items() if key not in SKIP_KEYS}


def sanitize_file_collections(config: Dict[str, Any]) -> List[List[str]]:
    return [
        [f"-{value}={it}"]
        for key, value in FILE_COLLECTION_KEYS.items()
        for it in config.get(key, [])
    ]


def sanitize_vars(variables: Dict[str, str]) -> List[List[str]]:
    return [["-var", f"{key}='{value}'"] for key, value in variables.items()]


def argument_pairs(config: Dict[str, Any]) -> List[List[str]]:
    return (
        [
            [f"-{key}={str(value)}"]
            for key, value in sanitize_config(config).items()
            if value
        ]
        + sanitize_file_collections(config)
        + sanitize_vars(config.get("vars", dict()))
    )


def unpack(pairs: List[List[str]]) -> List[str]:
    return [it for pair in pairs for it in pair]


def width() -> int:
    return min(40, os.get_terminal_size().columns)
