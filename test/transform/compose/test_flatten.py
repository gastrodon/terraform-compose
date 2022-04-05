from typing import Dict, List

import pytest

from library.transform import compose

cases = [
    [
        {"hello": "world"},
        [(["hello"], "world")],
    ],
    [
        {"cute": "aww!", "gross": "eugh!!!"},
        [(["cute"], "aww!"), (["gross"], "eugh!!!")],
    ],
    [
        {"favorite": "hugh", "contendors": ["hugh", "edward", "pixie", "alice"]},
        [
            (["favorite"], "hugh"),
            (["contendors", 0], "hugh"),
            (["contendors", 1], "edward"),
            (["contendors", 2], "pixie"),
            (["contendors", 3], "alice"),
        ],
    ],
    [
        {
            "everybody": [
                {"nest": "friends"},
                {"nest": "nemesis"},
            ]
        },
        [
            (["everybody", 0, "nest"], "friends"),
            (["everybody", 1, "nest"], "nemesis"),
        ],
    ],
    [
        {
            "books": {
                "haskel": {"thought": "funny elephant"},
                "elm": {"thought": "omg i love trees"},
                "rust": {"thought": "i am a homosexual"},
            },
            "songs": [
                "elevator",
                "crush bang",
                "2012 indie",
            ],
        },
        [
            (["books", "haskel", "thought"], "funny elephant"),
            (["books", "elm", "thought"], "omg i love trees"),
            (["books", "rust", "thought"], "i am a homosexual"),
            (["songs", 0], "elevator"),
            (["songs", 1], "crush bang"),
            (["songs", 2], "2012 indie"),
        ],
    ],
    [
        ["hello", "every", "body"],
        [
            ([0], "hello"),
            ([1], "every"),
            ([2], "body"),
        ],
    ],
    [
        ("hello", "you", "!"),
        [
            ([0], "hello"),
            ([1], "you"),
            ([2], "!"),
        ],
    ],
    [
        ("alpha", "beta"),
        [
            ([0], "alpha"),
            ([1], "beta"),
        ],
    ],
]


@pytest.mark.parametrize("wide,want", cases)
def test_flatten(wide: Dict, want: List):
    assert compose.flatten(wide) == want
