from typing import Dict, List

import pytest

from library import cli, load
from library.model.compose import Compose
from library.resolve import resolve

cases_uncomplex = [
    [
        [],
        {"": {"service": {"hello": {"path": "./world"}}}},
        Compose(service={"hello": {"path": "/tf-compose/world"}}),
    ],
    [
        [],
        {"": {"service": {"hello": {"var-file": ["./foobar"]}}}},
        Compose(service={"hello": {"var-file": ["/tf-compose/foobar"]}}),
    ],
    [
        [],
        {"": {"service": {"hello": {"state-out": "./state"}}}},
        Compose(service={"hello": {"state-out": "/tf-compose/state"}}),
    ],
]

cases_import = [
    [
        [],
        {
            "": {"import": ["remote"]},
            "remote": {"service": {"hello": {"path": "./world"}}},
        },
        Compose(service={"remote.hello": {"path": "/tf-compose/remote/world"}}),
    ],
    [
        [],
        {
            "": {"import": ["remote"]},
            "remote": {"import": ["tiny"]},
            "remote.tiny": {"service": {"hello": {"path": "./world"}}},
        },
        Compose(
            service={"remote.tiny.hello": {"path": "/tf-compose/remote/tiny/world"}}
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
                "earth": {
                    "path": "/tf-compose/planet/earth",
                    "var": {"hello": "world"},
                },
                "venus": {
                    "path": "/tf-compose/planet/venus",
                    "var": {"hello": "world"},
                },
            }
        ),
    ]
]

cases_arguments = [
    [
        ["init", "-reconfigure"],
        {
            "": {
                "service": {
                    "earth": {"path": "./planet/earth"},
                    "venus": {"path": "./planet/venus"},
                }
            }
        },
        Compose(
            service={
                "earth": {
                    "path": "/tf-compose/planet/earth",
                    "reconfigure": True,
                },
                "venus": {
                    "path": "/tf-compose/planet/venus",
                    "reconfigure": True,
                },
            }
        ),
    ],
    [
        ["up", "-var-file", "./woomy"],
        {
            "": {
                "service": {
                    "earth": {"path": "./planet/earth", "var-file": ["splat"]},
                    "venus": {
                        "path": "./planet/venus",
                    },
                }
            }
        },
        Compose(
            service={
                "earth": {
                    "path": "/tf-compose/planet/earth",
                    "var-file": ["/tf-compose/splat", "/tf-compose/woomy"],
                },
                "venus": {
                    "path": "/tf-compose/planet/venus",
                    "var-file": ["/tf-compose/woomy"],
                },
            }
        ),
    ],
]

cases = [
    *cases_uncomplex,
    *cases_import,
    *cases_global,
    *cases_arguments,
]


@pytest.mark.parametrize("argv,resolution,want", cases)
def test_load(argv: List[str], resolution: Dict[str, Dict], want: Compose, mocker):
    mocker.patch("os.getcwd", return_value="/tf-compose")
    resolve.set(resolution)

    assert load.load(cli.arguments(argv), "") == want
