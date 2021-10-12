import abc
import enum
from abc import ABC
from enum import IntEnum

ERR_CIRCULAR_DEPENDS_ON = """\
{service} has a circular dependency!
    {path}
"""


class Codes(IntEnum):
    ERR_CIRCULAR_DEPENDS_ON: int = enum.auto()


class RenderException(ABC, Exception):
    @abc.abstractmethod
    def render(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def code(self) -> int:
        ...


class CircularDependsOn(RenderException):
    def __init__(self, service: str, parents: list[str]):
        self.message = ERR_CIRCULAR_DEPENDS_ON.format(
            service=service,
            path=" <- ".join((service, *parents)),
        )

        super().__init__(self.message)

    def render(self) -> str:
        return self.message

    @property
    def code(self) -> int:
        return Codes.ERR_CIRCULAR_DEPENDS_ON
