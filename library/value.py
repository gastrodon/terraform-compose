from typing import Dict

CONTEXT: str = ""
COMPOSE_FILE: str = "terraform-compose.yml"

TERRAFORM_OPTS: Dict = {
    "context": CONTEXT,
    "file": COMPOSE_FILE,
}
