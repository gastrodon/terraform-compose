from unittest import TestCase

from library.config.depends import tools

case_flatten_map = [
    {
        "have": {"hello": "world"},
        "want": {"hello": "world"},
        "prefix": "",
    },
    {
        "have": {"hello": "world"},
        "want": {"hello": "world"},
        "prefix": "",
    },
    {
        "have": {"hello": {"small": "world"}},
        "want": {"hello.small": "world"},
        "prefix": "",
    },
    {
        "have": {"hello": "world"},
        "want": {"space.hello": "world"},
        "prefix": "space",
    },
    {
        "have": {"hello": {"small": "world"}},
        "want": {"hello.small": "world"},
        "prefix": "",
    },
    {
        "have": {"hello": {"small": "world"}},
        "want": {"friendly.hello.small": "world"},
        "prefix": "friendly",
    },
]


class TestFlattenMap(TestCase):
    def test_flatten_map(self):
        for index, case in enumerate(case_flatten_map):
            flat = tools.flatten_map(
                case["have"],
                prefix=case["prefix"],
            )

            if flat != case["want"]:
                raise AssertionError(f"Case #{index+1} produced {flat}")
