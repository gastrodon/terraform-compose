from typing import Dict

from transform import compose

path_matchers = [
    [None, "@(.+)$"],
    [r"service\..+\.path$", None],
    [r"service\..+\.backend_config\.\d+$", None],
    [r"service\..+\.state\.\d+$", None],
    [r"service\..+\.state_out\.\d+$", None],
    [r"service\..+\.var_file\.\d+$", None],
    [r"service\..+\.backup\.\d+$", None],
]


def absolutize_single(value: str):
    ...  # TODO


def absolutize(service: Dict) -> Dict:
    return merge(
        service,
        {
            key: absolutize_single(value)
            for matcher in path_matchers
            for key, value in compose.find(service, *matcher).items()  # TODO
        },
    )
