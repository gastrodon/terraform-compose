from typing import Dict

CONTEXT: str = ""
COMPOSE_FILE: str = "terraform-compose.yml"


TERRAFORM_EXECUTABLE: str = "terraform"
TERRAFORM_PLAN_FILE: str = "tf-compose-plan"
TERRAFORM_OPTS: Dict = {
    "context": CONTEXT,
    "file": COMPOSE_FILE,
}
