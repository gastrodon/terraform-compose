from typer import Option

file: Option = Option(
    "terraform-compose.yml", "-f", "--file", help="Compose file top read"
)
graph: Option = Option(False, "-g", "--graph", help="Draw dependency graphs")
services: Option = Option(
    None, "-s", "--services", help="Services to target. Can be used multiple times"
)
upgrade: Option = Option(
    False, "-u", "--upgrade", "Upgrade terraform providers and modules"
)
