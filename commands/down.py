import typer

import app


@app.app.command()
async def down():
    typer.echo("down")
