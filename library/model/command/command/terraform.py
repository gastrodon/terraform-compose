from library.model.command.base import Command


class Terraform(Command):
    name = "terraform"
    kv = ["context", "file"]
    listy = ["service"]
