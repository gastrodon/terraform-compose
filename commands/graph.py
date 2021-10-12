import typer

import app


@app.app.command()
async def graph():
    typer.echo("graph")
