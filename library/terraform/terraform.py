import json  # noqa
from json import JSONEncoder
from os import path
from typing import Any, Callable, Dict, List

import python_terraform

from library.types.kind import Kind

PATH_KEYS: List[str] = [
    "state-backup",
    "state-out",
    "state",
]

SKIP_KEYS: List[str] = ["plan", "path", "var-files"]


class EncodeSet(JSONEncoder):
    def default(self, it):
        return list(it) if isinstance(it, set) else JSONEncoder.default(it)


def make_callable(kind: Kind, **kwargs: Dict[str, Any]) -> Callable:
    handle = python_terraform.Terraform(**kwargs)

    return {
        Kind.apply.name: handle.apply,
        Kind.destroy.name: handle.destroy,
        Kind.plan.name: handle.plan,
    }[kind]


def sanitize_config(config: Dict[str, Any]) -> Dict[str, Any]:
    paths_relative = {
        key: path.join(config["path"], config[key])
        if path.isabs(config[key])
        else config[key]
        for key in PATH_KEYS
        if key in config.keys()
    }

    return {
        key.replace("-", "_"): value
        for key, value in {**config, **paths_relative}.items()
        if key not in SKIP_KEYS
    }


def do(
    kind: Kind,
    service: str,
    args: List[str],
    config: Dict[str, Any],
) -> (int, str, str):
    var_files = [
        path.join(config["path"], it) if path.isabs(it) else it
        for it in config["var-files"]
    ]

    callable = make_callable(kind.name, working_dir=config["path"], var_file=var_files)
    return callable(*args, **sanitize_config(config))
