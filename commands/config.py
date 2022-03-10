from app import app
from library import config


@app.command(name="config")
def handle(file: str):
    print(config.from_file([], file))
