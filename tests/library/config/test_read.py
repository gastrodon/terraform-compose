from unittest import TestCase

from library import config
from library.config.defaults import PLAN
from library.types.exceptions import ValidateFailed


class TestRead(TestCase):
    """
    Test read
    """

    def test_read_plan(self):
        part = {
            "path": ".",
            "refresh-only": True,
            "target": "service-name",
            "var-files": ["./foo/bar.tfvar"],
            "vars": {
                "var": "foobar",
                "bengis": "hello",
            },
        }

        service_config = {
            **part,
            "input": False,
            "json": True,
            "refresh": False,
            "replace": None,
        }

        name = "name"
        compose = {"services": {name: part}}

        try:
            assert config.read(PLAN, name, compose) == service_config
        except ValidateFailed as err:
            raise Exception(err.render)

    def test_read_plan_fail(self):
        name = "name"
        part = {"path": ".", "var-files": "foobar"}
        compose = {"services": {name: part}}

        try:
            config.read(PLAN, name, compose)
            raise AssertionError

        except ValidateFailed as err:
            assert err.service == name
            assert err.key == "var-files"
            assert err.value == part["var-files"]
