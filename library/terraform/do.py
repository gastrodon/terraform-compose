import json
import subprocess
from typing import Any, Dict, List

import typer

from library.pretty import Status
from library.terraform import tools
from library.types.kind import Kind


def do(kind: Kind, args: List[str], config: Dict[str, Any]) -> (int, str, str):
    arguments = [
        "terraform",
        f"-chdir={config['path']}",
        kind.name,
        *tools.unpack(tools.argument_pairs(config)),
        *args,
    ]

    ran = subprocess.run(arguments, capture_output=True, text=True)
    return ran.returncode, ran.stdout, ran.stderr


def do_up(config_set: Dict[str, Any]) -> (int, str, str):
    status = Status(config_set["service"])
    typer.echo(status.render(tools.width()))

    if config_set["destroy"]:
        code, stdout, stderr = do(
            Kind.show,
            ["-json"],
            {"path": config_set["plan"]["kwargs"]["path"]},
        )

        if not json.loads(stdout).get("values"):
            typer.echo(status.phase_next().skip().render(tools.width()))
            return code, "", stderr

    code, stdout, stderr = do(
        Kind.plan,
        config_set["plan"]["args"],
        config_set["plan"]["kwargs"],
    )

    if code:
        raise Exception(
            "\n\n".join(
                filter(
                    bool,
                    [f"terraform exited with code {code}", stdout, stderr],
                )
            )
        )

    typer.echo(status.phase_next().render(tools.width()))

    code, stdout, stderr = do(
        Kind.apply,
        config_set["apply"]["args"],
        config_set["apply"]["kwargs"],
    )

    typer.echo(status.finish().render(tools.width()))
    return code, stdout, stderr
