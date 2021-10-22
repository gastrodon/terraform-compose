from multiprocessing import Pool
from typing import Any, Dict, List

import typer

import app
from library import config, terraform
from library.config.defaults import REFRESH
from library.pretty import Status
from library.terraform import tools
from library.types import options
from library.types.kind import Kind


def refresh_wrapped(config: Dict[str, Any]):
    status: Status = Status(config["name"], phases=["refreshing"])
    typer.echo(status.render(tools.width()))

    terraform.do(Kind.refresh, config["args"], config["kwargs"])

    typer.echo(status.finish().render(tools.width()))


@app.app.command(name="refresh")
def handle_refresh(
    services: List[str] = options.services,
    file: str = options.file,
):
    compose = config.read_file(file)
    services = services or compose["services"].keys()

    configs = [
        {
            "name": service,
            "args": [],
            "kwargs": config.read(REFRESH, service, compose),
        }
        for service in services
    ]

    with Pool(processes=len(configs)) as pool:
        pool.map(refresh_wrapped, configs)
