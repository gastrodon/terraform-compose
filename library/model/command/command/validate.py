from library.model.command.base import Command


class Validate(Command):
    name = "validate"
    flag = ["json", "no-color"]
