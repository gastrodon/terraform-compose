#!/usr/bin/env python3
from os import sys

from library import cli, load, resolve


def main():
    resolve.gather()

    loaded = load.load(cli.arguments(sys.argv[1:]), "")

    print(loaded)


if __name__ == "__main__":
    main()
