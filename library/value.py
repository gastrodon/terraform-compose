from typing import Dict

CONTEXT_PATH: str = ""
COMPOSE_FILE: str = "terraform-compose.yml"

TERRAFORM_OPTS: Dict = {
    "context": CONTEXT_PATH,
    "file": COMPOSE_FILE,
}
