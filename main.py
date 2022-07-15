#!/usr/bin/env python3
from os import sys

from library import cli, execute, resolve, value
from library.model.cli import ArgumentScope
from library.transform import compose


def main():
    arguments = cli.arguments(sys.argv[1:])

    terraform_opts = compose.merge(
        value.TERRAFORM_OPTS,
        cli.collect(arguments, ArgumentScope.terraform),
    )

    resolve.gather("", terraform_opts["context"], terraform_opts["file"])
    execute.execute("", arguments, terraform_opts)


if __name__ == "__main__":
    main()
