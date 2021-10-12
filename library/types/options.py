from typer import Option

file: Option = Option("terraform-compose.yml", "-f", "--file")
service: Option = Option(..., "-s", "--service")
