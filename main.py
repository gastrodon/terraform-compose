#!/usr/bin/env python3
from os import sys

import typer
import yaml
from typer import colors

import library
from library.types import options
from library.types.exceptions import RenderException


def main_wrap(file: str = options.file, service: str = options.service):
    try:
        return main(file, service)

    except RenderException as err:
        typer.secho(err.render(), fg=colors.RED, err=True)
        sys.exit(err.code)


def main(file: str = options.file, service: str = options.service):
    with open(file) as stream:
        config = yaml.safe_load(stream)

    typer.echo(library.dependency_tree(service, config["services"]))


if __name__ == "__main__":
    typer.run(main_wrap)
