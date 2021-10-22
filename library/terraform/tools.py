import os
from os import path
from typing import Any, Dict, List

PATH_KEYS: List[str] = [
    "state-backup",
    "state-out",
    "state",
]

SKIP_KEYS: List[str] = ["plan", "path", "var-files", "vars"]


def sanitize_config(config: Dict[str, Any]) -> Dict[str, Any]:
    paths_relative = {
        key: path.join(config["path"], config[key])
        if not path.isabs(config[key])
        else config[key]
        for key in PATH_KEYS
        if key in config.keys()
        if config[key]
    }

    return {
        key: value
        for key, value in {**config, **paths_relative}.items()
        if key not in SKIP_KEYS
    }


def sanitize_var_files(root: str, files: List[str]) -> List[List[str]]:
    return [
        ["-var-file", path.join(root, it) if not path.isabs(it) else it] for it in files
    ]


def sanitize_vars(variables: Dict[str, str]) -> List[List[str]]:
    return [["-var", f"{key}='{value}'"] for key, value in variables.items()]


def argument_pairs(config: Dict[str, Any]) -> List[List[str]]:
    return (
        [
            [f"-{key}", str(value)]
            for key, value in sanitize_config(config).items()
            if value
        ]
        + sanitize_var_files(config["path"], config.get("var-files", []))
        + sanitize_vars(config.get("vars", dict()))
    )


def unpack(pairs: List[List[str]]) -> List[str]:
    return [it for pair in pairs for it in pair]


def width() -> int:
    return min(40, os.get_terminal_size().columns)
