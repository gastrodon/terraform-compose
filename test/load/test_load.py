from typing import Dict, List

import pytest

from library import load
from library.model import Compose, Config
from library.resolve import resolve

cases_uncomplex = [
    [
        [],
        {"": {"service": {"hello": {"path": "./world"}}}},
        Compose(service={"hello": Config(path="/tf-compose/world")}),
    ],
]

cases_import = [
    [
        [],
        {
            "": {"import": ["remote"]},
            "remote": {"service": {"hello": {"path": "./world"}}},
        },
        Compose(service={"remote.hello": Config(path="/tf-compose/remote/world")}),
    ],
    [
        [],
        {
            "": {"import": ["remote"]},
            "remote": {"import": ["tiny"]},
            "remote.tiny": {"service": {"hello": {"path": "./world"}}},
        },
        Compose(
            service={"remote.tiny.hello": Config(path="/tf-compose/remote/tiny/world")}
        ),
    ],
]

cases_global = [
    [
        [],
        {
            "": {
                "global": {"var": {"hello": "world"}},
                "service": {
                    "earth": {"path": "./planet/earth"},
                    "venus": {"path": "./planet/venus"},
                },
            }
        },
        Compose(
            service={
                "earth": Config(
                    path="/tf-compose/planet/earth", var={"hello": "world"}
                ),
                "venus": Config(
                    path="/tf-compose/planet/earth", var={"hello": "world"}
                ),
            }
        ),
    ]
]

cases = [
    *cases_uncomplex,
    *cases_import,
]


@pytest.mark.parametrize("args,resolution,want", cases)
def test_load(args: List, resolution: Dict[str, Dict], want: Compose, mocker):
    mocker.patch("os.getcwd", return_value="/tf-compose")
    resolve.set(resolution)

    assert load.load(args, "") == want
