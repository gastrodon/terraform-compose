import typer

import app


@app.app.command()
def down():
    typer.echo("down")
