import typer

import app


@app.app.command()
def graph():
    typer.echo("graph")
