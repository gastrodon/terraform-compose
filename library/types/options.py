from typer import Option

actions: Option = Option(
    None, "-a", "--actions", help="Actions to target. Can be used multiple times"
)
file: Option = Option(
    "terraform-compose.yml", "-f", "--file", help="Compose file top read"
)
graph: Option = Option(False, "-g", "--graph", help="Draw dependency graphs")
services: Option = Option(
    None, "-s", "--services", help="Services to target. Can be used multiple times"
)
upgrade: Option = Option(
    False, "-u", "--upgrade", help="Upgrade terraform providers and modules"
)
destroy: Option = Option(
    False, "--destroy", help="Destroy resources instead of creating them"
)
