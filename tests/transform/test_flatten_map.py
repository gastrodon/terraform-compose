from unittest import TestCase

from library.config.depends import tools

case_flatten_map = [
    {
        "have": {"hello": "world"},
        "want": {"hello": "world"},
        "prefix": "",
        "keep_sub": False,
    },
    {
        "have": {"hello": "world"},
        "want": {"hello": "world"},
        "prefix": "",
        "keep_sub": True,
    },
    {
        "have": {"hello": {"small": "world"}},
        "want": {"hello.small": "world"},
        "prefix": "",
        "keep_sub": False,
    },
    {
        "have": {"hello": "world"},
        "want": {"space.hello": "world"},
        "prefix": "space",
        "keep_sub": False,
    },
    {
        "have": {"hello": {"small": "world"}},
        "want": {"hello.small": "world", "hello": {"small": "world"}},
        "prefix": "",
        "keep_sub": True,
    },
    {
        "have": {"hello": {"small": "world"}},
        "want": {"friendly.hello.small": "world", "friendly.hello": {"small": "world"}},
        "prefix": "friendly",
        "keep_sub": True,
    },
]


class TestFlattenMap(TestCase):
    def test_flatten_map(self):
        for index, case in enumerate(case_flatten_map):
            flat = tools.flatten_map(
                case["have"],
                prefix=case["prefix"],
                keep_sub=case["keep_sub"],
            )

            if flat != case["want"]:
                raise AssertionError(f"Case #{index+1} produced {flat}")
