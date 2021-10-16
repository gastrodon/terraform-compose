from os import path
from typing import Any, Dict, List

import python_terraform

from library.types.kind import Kind

PATH_KEYS: List[str] = [
    "state-backup",
    "state-out",
    "state",
]

SKIP_KEYS: List[str] = ["plan", "path", "var-files"]


def do_plan(args: List[str], config: Dict[str, Any]) -> (int, str, str):
    var_files = [
        path.join(config["path"], it) if path.isabs(it) else it
        for it in config.get("var-files") or []
    ]

    handle = python_terraform.Terraform(working_dir=config["path"], var_file=var_files)
    return handle.plan(*args, **sanitize_config(config))


def do_apply(args: List[str], config: Dict[str, Any]) -> (int, str, str):
    handle = python_terraform.Terraform(working_dir=config["path"])
    return handle.plan(*args, **sanitize_config(config))


def sanitize_config(config: Dict[str, Any]) -> Dict[str, Any]:
    paths_relative = {
        key: path.join(config["path"], config[key])
        if path.isabs(config[key])
        else config[key]
        for key in PATH_KEYS
        if key in config.keys()
        if config[key]
    }

    return {
        key.replace("-", "_"): value
        for key, value in {**config, **paths_relative}.items()
        if key not in SKIP_KEYS
    }


def do(kind: Kind, args: List[str], config: Dict[str, Any]) -> (int, str, str):
    if kind == Kind.plan:
        return do_plan(args, config)

    if kind == Kind.apply:
        return do_plan(args, config)
