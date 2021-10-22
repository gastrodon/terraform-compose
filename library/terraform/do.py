import subprocess
from typing import Any, Dict, List

import typer

from library.pretty import Status
from library.terraform import tools
from library.types.kind import Kind


def do_plan(args: List[str], config: Dict[str, Any]) -> (int, str, str):
    arguments = [
        "terraform",
        f"-chdir={config['path']}",
        "plan",
        *tools.unpack(tools.argument_pairs(config)),
        *args,
    ]

    ran = subprocess.run(arguments, capture_output=True, text=True)
    return ran.returncode, ran.stdout, ran.stderr


def do_apply(args: List[str], config: Dict[str, Any]) -> (int, str, str):
    arguments = [
        "terraform",
        f"-chdir={config['path']}",
        "apply",
        *tools.unpack(tools.argument_pairs(config)),
        *args,
    ]

    ran = subprocess.run(arguments, capture_output=True, text=True)
    return ran.returncode, ran.stdout, ran.stderr


def do_init(args: List[str], config: Dict[str, Any]) -> (int, str, str):
    arguments = [
        "terraform",
        f"-chdir={config['path']}",
        "init",
        *tools.unpack(tools.argument_pairs(config)),
        *args,
    ]

    ran = subprocess.run(arguments, capture_output=True, text=True)
    return ran.returncode, ran.stdout, ran.stderr


def do(kind: Kind, args: List[str], config: Dict[str, Any]) -> (int, str, str):
    return {
        Kind.apply: do_apply,
        Kind.init: do_init,
        Kind.plan: do_plan,
    }(args, config)


def do_up(config_set: Dict[str, Any]) -> (int, str, str):
    status = Status(config_set["service"])
    typer.echo(status.render(tools.width()))

    code, stdout, stderr = do_plan(
        config_set["plan"]["args"],
        config_set["plan"]["kwargs"],
    )

    if code:
        raise Exception(
            "\n\n".join(
                filter(
                    lambda it: it,
                    [f"terraform exited with code {code}", stdout, stderr],
                )
            )
        )

    typer.echo(status.phase_next().render(tools.width()))

    code, stdout, stderr = do_apply(
        config_set["apply"]["args"],
        config_set["apply"]["kwargs"],
    )

    typer.echo(status.finish().render(tools.width()))
    return code, stdout, stderr
