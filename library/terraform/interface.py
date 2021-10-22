import os
from typing import Any, Dict

import typer

from library.pretty.status import Status
from library.terraform import terraform


def width() -> int:
    return min(40, os.get_terminal_size().columns)


def do_up(config_set: Dict[str, Any]) -> (int, str, str):
    status = Status(config_set["service"])
    typer.echo(status.render(width()))

    code, stdout, stderr = terraform.do_plan(
        config_set["plan"]["args"],
        config_set["plan"]["kwargs"],
    )

    if code:
        return code, stdout, stderr

    typer.echo(status.phase_next().render(width()))

    code, stdout, stderr = terraform.do_apply(
        config_set["apply"]["args"],
        config_set["apply"]["kwargs"],
    )

    typer.echo(status.finish().render(width()))
    return code, stdout, stderr
