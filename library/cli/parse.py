from typing import List, Type

ArgumentPart = Type  # TODO


def consume(tokens: List[str]) -> ArgumentPart:
    """
    Given a segment of tokens, consume them and produce a useful ArgumentPart
    """
    return f"consume({tokens})"


def segment(tokens: List[str]) -> int:
    """
    Given a collection of tokens,
    return number of tokens  that constitute the first consumable part
    """
    return 1


def parse(tokens: List[str]):
    """
    Given a space-split segment of raw arguments, step through and parse them

    for every token that we step to we'll get a segment count :n,
    and consume the token and :n following tokens

    the product of consuming tokens are collected and update parsing state, for example
        - consuming the command will end global collecting
        - consuming the -- token will start key => value collecting
    """
    argument_parts: List[ArgumentPart] = []
    index: int = 0

    while index < len(tokens):
        end = segment(tokens)
        argument_parts += [consume(tokens[index : index + end])]

        index += end

    return argument_parts
