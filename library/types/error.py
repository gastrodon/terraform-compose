import enum
import os
from enum import IntEnum
from os import sys
from typing import Any

IS_TEST = os.getenv("IS_TEST") == "true"


error_depends = """\
{service} has a circular dependency chain!
    path: {path}
"""

Type = Any


class Codes(IntEnum):
    VALIDATION = enum.auto()
    DEPENDS = enum.auto()


class RenderException(Exception):
    def exit(self):
        with open("/dev/stderr", "w") as stream:
            stream.write(self.render)

        if IS_TEST:
            raise self

        sys.exit(self.code)  # pragma: not covered

    @property
    def render(self) -> str:
        return self._render

    @property
    def code(self) -> int:
        return self._code


class ValidationError(RenderException):
    _code = Codes.VALIDATION

    def __init__(self, message: str):
        super().__init(message)

        self._render = message


class DependsError(RenderException):
    _code = Codes.DEPENDS

    def __init__(self, service: str, parents: list[str]):
        self.service = service
        self.parents = parents

        self._render = error_depends.format(
            service=service,
            path=" -> ".join((*parents, service)),
        )

        super().__init__(self._render)
