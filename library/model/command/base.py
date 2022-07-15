from __future__ import annotations

from typing import Any

from library.cli import parse
from library.model.cli.argument import Argument
from library.model.cli.kind import ArgumentKind
from library.model.cli.parse import ArgumentParser


def many(many: list[Any], one: Any) -> dict[Any, Any]:
    if callable(one):
        return {each: one() for each in many}
    return {each: one for each in many}


class Command:
    name: str
    kv: list[str] = []
    flag: list[str] = []
    listy: list[str] = []
    dicty: list[str] = []
    extra: dict[str, ArgumentParser] = {}

    @classmethod
    def arguments(cls: Command) -> dict[str, Argument]:
        """A collection of key: value arguments"""
        return {
            **many(
                cls.kv,
                ArgumentParser(ArgumentKind.kv, commands={cls.name}),
            ),
            **many(
                cls.flag,
                ArgumentParser(ArgumentKind.flag, False, commands={cls.name}),
            ),
            **many(
                cls.listy,
                ArgumentParser(
                    ArgumentKind.flag, list(), parser=parse.listy, commands={cls.name}
                ),
            ),
            **many(
                cls.dicty,
                ArgumentParser(
                    ArgumentKind.flag, dict(), parser=parse.dicty, commands={cls.name}
                ),
            ),
            **cls.extra,
        }
