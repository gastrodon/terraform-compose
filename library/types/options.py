from typer import Option

file: Option = Option("terraform-compose.yml", "-f", "--file")
services: Option = Option(None, "-s", "--services")
