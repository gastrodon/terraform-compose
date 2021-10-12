import typer

import app
from library import depends as lib_depends, load
from library.types import options


@app.app.command()
def depends(
    file: str = options.file,
    service: str = options.service,
):
    config = load.from_name(file)

    typer.echo(
        lib_depends.render(
            lib_depends.tree(service, config["services"]),
        )
    )
