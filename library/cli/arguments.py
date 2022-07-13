from typing import List

from library.cli.compress import compress
from library.cli.sort import sort
from library.model.cli import (
    Argument,
    ArgumentCommand,
    ArgumentFlag,
    ArgumentKV,
    ArgumentScope,
    ArgumentSeparator,
)
from library.model.cli import ArgumentKind
from library.model.cli.parse import ParseContext, Parser
from library.model.command import CommandKind
from library.model.command.kind import COMMAND_KIND_LOOKUP

def update(
    context: ParseContext,
    skip: int = 0,
    scope: ArgumentScope = None,
    command: CommandKind = None,
) -> ParseContext:
    return ParseContext(
        context.tokens[skip:],
        scope or context.scope,
        command or context.command,
    )


def require_kv(tokens: List[str]):
    if len(tokens) == 1:
        raise ValueError(f"argument {tokens[0]} requires a value!")


def next_command(context: ParseContext) -> (ArgumentCommand, List[str]):
    if context.command is not CommandKind.terraform:
        raise ValueError(
            f"don't know what to do with {context.tokens[0]},"
            f"already have command {context.command.name}"
        )

    try:
        command = COMMAND_KIND_LOOKUP[context.tokens[0]]

        return (
            ArgumentCommand(context.tokens[0]),
            update(context, skip=1, command=command, scope=ArgumentScope.command),
        )

    except KeyError:
        raise ValueError(f"no such command {context.tokens[0]}!")


def next_named(context: ParseContext) -> (Argument, ParseContext):
    if context.scope is ArgumentScope.compose:
        require_kv(context.tokens)
        return (
            ArgumentKV(context.tokens[0], context.tokens[1], context.scope),
            update(context, skip=2),
        )

    name = context.tokens[0].removeprefix("-")
    parser = context.command.value.arguments().get(name)
    if not parser:
        raise Exception(f"{context.command.name} can't parse {name}!")

    match parser.kind:
        case ArgumentKind.kv:
            require_kv(context.tokens)
            return (
                ArgumentKV(name, parser.parse(context.tokens[1]), context.scope),
                update(context, skip=2),
            )
        case ArgumentKind.flag:
            return (
                ArgumentFlag(name, context.scope),
                update(context, skip=1),
            )
        case _:
            raise Exception(f"{context.command.name} has unknown kind {parser.kind}!")


def next_argument(context: ParseContext) -> (Argument, ParseContext):
    if not context.tokens:
        raise ValueError("no tokens to read!")

    if context.tokens[0] == "--":
        return ArgumentSeparator(), update(context, skip=1, scope=ArgumentScope.compose)

    if context.tokens[0].startswith("-") or context.scope is ArgumentScope.compose:
        return next_named(context)

    return next_command(context)


def arguments(tokens: List[str]) -> List[Argument]:
    context = ParseContext([*tokens], ArgumentScope.terraform, CommandKind.terraform)
    collection = []

    while context.tokens:
        next, context = next_argument(context)
        collection += [next]

    return sort(
        [
            compressed
            for scope in [ArgumentScope.terraform, ArgumentScope.command, ArgumentScope.compose]
            for compressed in filter(lambda it: it.scope == scope, compress(collection, scope))
        ]
    )
