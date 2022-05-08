import functools
import os
from typing import Dict, List, Union

from library.transform import compose

path_matchers = [
    [r"^service\..*", "^@.+$"],
    [r"^service\..+\.path$", None],
    [r"^service\..+\.backend_config$", None],
    [r"^service\..+\.state$", None],
    [r"^service\..+\.state_out$", None],
    [r"^service\..+\.var_file$", None],
    [r"^service\..+\.backup$", None],
]


def absolutize_single(service_name: str, value: Union[List[str], str]) -> str:
    service_path = service_name.split(".")[:-1]

    if isinstance(value, list):
        return [absolutize_single(service_name, it) for it in value]

    if value.startswith("@"):
        return "@" + os.path.realpath(os.path.join(*service_path, value[1:]))

    return os.path.realpath(os.path.join(*service_path, value))


def absolutize(service: Dict) -> Dict:
    insertions = [
        (path, absolutize_single(path[1], compose.resolve(service, path)))
        for matcher in path_matchers
        for path in compose.find(service, matcher[0], matcher[1], lists=False)
    ]

    return functools.reduce(
        lambda last, insertion: compose.insert(last, insertion[0], insertion[1]),
        [service, *insertions],
    )
