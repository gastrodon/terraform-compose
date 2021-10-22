from multiprocessing import Pool
from typing import Any, Dict, List

import typer

import app
from library import config, terraform
from library.config.defaults import INIT
from library.pretty import Status
from library.terraform import tools
from library.types import options
from library.types.kind import Kind


def init_wrapped(config: Dict[str, Any]):
    status: Status = Status(config["name"], phases=["initing"])
    typer.echo(status.render(tools.width()))

    terraform.do(Kind.init, config["args"], config["kwargs"])

    typer.echo(status.finish().render(tools.width()))


@app.app.command(name="init")
def handle_init(
    services: List[str] = options.services,
    file: str = options.file,
    upgrade: bool = options.upgrade,
):
    compose = config.read_file(file)
    services = services or compose["services"].keys()

    configs = [
        {
            "name": service,
            "args": [],
            "kwargs": {**config.read(INIT, service, compose), "upgrade": upgrade},
        }
        for service in services
    ]

    with Pool(processes=len(configs)) as pool:
        pool.map(init_wrapped, configs)
