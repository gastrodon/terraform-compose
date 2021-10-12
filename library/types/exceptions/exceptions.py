import enum
from enum import IntEnum
from os import sys

import typer
from typer import color

ERR_CIRCULAR_DEPENDS_ON = """\
{service} has a circular dependency!
    {path}"""


class Codes(IntEnum):
    ERR_CIRCULAR_DEPENDS_ON: int = enum.auto()


class RenderException(Exception):
    def exit(self):  # TODO allow for not exiting when testing
        typer.secho(self.render, color=color.RED, err=True)
        sys.exit(self.code)

    @property
    def render(self) -> str:
        return self._render

    @property
    def code(self) -> int:
        return self._code


class CircularDependsOn(RenderException):
    _code = Codes.ERR_CIRCULAR_DEPENDS_ON

    def __init__(self, service: str, parents: list[str]):
        self._render = ERR_CIRCULAR_DEPENDS_ON.format(
            service=service,
            path=" -> ".join((*parents, service)),
        )

        super().__init__(self._render)
