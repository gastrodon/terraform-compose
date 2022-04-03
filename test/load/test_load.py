from library import load
from library.model import Compose, Config
from library.resolve import resolve

cases_uncomplex = [
    {
        "resolve": {"": {"services": {"hello": {"path": "./world"}}}},
        "want": Compose(services={"hello": Config(path="./world")}),
    }
]

cases_import = [
    {
        "resolve": {
            "": {"import": ["remote"]},
            "remote": {"services": {"hello": {"path": "./world"}}},
        },
        "want": Compose(services={"remote.hello": Config(path="./world")}),
    },
    {
        "resolve": {
            "": {"import": ["remote"]},
            "remote": {"import": ["tiny"]},
            "remote.tiny": {"services": {"hello": {"path": "./world"}}},
        },
        "want": Compose(services={"remote.tiny.hello": Config(path="./world")}),
    },
]

cases_global = [
    {
        "resolve": {
            "": {
                "global": {"var": {"hello": "world"}},
                "services": {
                    "earth": {"path": "./planet/earth"},
                    "venus": {"path": "./planet/venus"},
                },
            }
        },
        "want": Compose(
            services={
                "earth": Config(path="./planet/earth", var={"hello": "world"}),
                "venus": Config(path="./planet/earth", var={"hello": "world"}),
            }
        ),
    }
]

cases = [
    *cases_uncomplex,
    *cases_import,
]


def test_load():
    for index, case in enumerate(cases):
        resolve.set(case["resolve"])

        assert load.load(case.get("args", []), "") == case["want"], f"cases[{index}]"
