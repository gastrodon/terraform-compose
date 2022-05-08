from typing import List

from library.model.cli import (
    Argument,
    ArgumentCommand,
    ArgumentKV,
    ArgumentScope,
    ArgumentSeparator,
)


def next_command(tokens: List[str]) -> (ArgumentCommand, List[str]):
    try:
        return ArgumentCommand(tokens[0]), tokens[1:]
    except KeyError:
        raise ValueError(f"no such command {tokens[0]}!")


def next_named(tokens: List[str], scope: ArgumentScope) -> (Argument, List[str]):
    # TODO check that we're not going to overflow on the second token
    # TODO check if this is actually a flag ( need a lookup table )
    return ArgumentKV(tokens[0].removeprefix("-"), tokens[1], scope), tokens[2:]


def next_argument(tokens: List[str], scope: ArgumentScope) -> (Argument, List[str]):
    if not tokens:
        raise ValueError("no tokens to read!")

    if tokens[0] == "--":
        return ArgumentSeparator(), tokens[1:]

    if tokens[0].startswith("-") or scope is ArgumentScope.compose:
        return next_named(tokens, scope)

    return next_command(tokens)


def arguments(tokens: List[str]) -> List[Argument]:
    tokens_remain = [*tokens]
    collection = []

    scope = ArgumentScope.terraform

    while tokens_remain:
        next, tokens_remain = next_argument(tokens_remain, scope)
        collection += [next]
        scope = next.scope

    return collection
