from typing import List

from library.model.cli.argument import Argument, ArgumentCommand, ArgumentSeparator


def argument_next_command(tokens: List[str]) -> (ArgumentCommand, List[str]):
    try:
        return ArgumentCommand(tokens[0]), tokens[1:]
    except KeyError:
        raise ValueError(f"no such command {tokens[0]}!")


def arguments_next_pair(tokens: List[str]) -> (Argument, List[str]):
    # TODO check that we're not going to overflow on the second token
    # TODO check if this is actually a flag ( need a lookup table )
    return Argument(tokens[0].removeprefix("-"), tokens[1]), tokens[2:]


def argument_next(tokens: List[str], did_separate: bool) -> (Argument, List[str]):
    if not tokens:
        raise ValueError("no tokens to read!")

    if tokens[0] == "--":
        return ArgumentSeparator(), tokens[1:]

    if tokens[0].startswith("-") or did_separate:
        return arguments_next_pair(tokens)

    return argument_next_command(tokens)


def collect_arguments(tokens: List[str]) -> List[Argument]:
    did_separate = False
    tokens_remain = [*tokens]
    collection = []

    while tokens_remain:
        next, tokens_remain = argument_next(tokens_remain, did_separate)
        collection += [next]

        if isinstance(next, ArgumentSeparator):
            did_separate = True

    return collection
