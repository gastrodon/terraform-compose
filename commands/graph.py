import typer

app = typer.Typer()


@app.command
def graph():
    typer.echo("graph")
