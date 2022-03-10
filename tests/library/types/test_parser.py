from unittest import TestCase

from pydantic import ValidationError

from library.types.config import Config
from library.types.parser import Parser


class TestParser(TestCase):
    """
    Test yaml config parsing into a Config
    """

    def test_parser_loads(self):
        source = """
        services:
            foobar:
                no-destroy: yes
        """

        target = {"foobar": Config(no_destroy=True)}

        assert Parser().raw([], source)["foobar"].no_destroy

    def test_parser_fails_on_type(self):
        source = """
        services:
            foobar:
                no-destroy: oops
        """

        try:
            Parser().raw([], source)

            raise AssertionError("Parser.raw didn't raise")
        except ValidationError:
            return
