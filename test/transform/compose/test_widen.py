from typing import Dict, List

import pytest

from library.transform import compose

cases = [
    [
        [(["hello"], "world")],
        {"hello": "world"},
    ],
    [
        [
            (["books", "haskel", "thought"], "funny elephant"),
            (["books", "elm", "thought"], "omg i love trees"),
            (["books", "rust", "thought"], "i am a transexual"),
            (["songs", 0], "elevator"),
            (["songs", 1], "crush bang"),
            (["songs", 2], "2012 indie"),
        ],
        {
            "books": {
                "haskel": {"thought": "funny elephant"},
                "elm": {"thought": "omg i love trees"},
                "rust": {"thought": "i am a transexual"},
            },
            "songs": [
                "elevator",
                "crush bang",
                "2012 indie",
            ],
        },
    ],
]


@pytest.mark.parametrize("flat,want", cases)
def test_flatten(flat: List, want: Dict):
    assert compose.widen(flat) == want
