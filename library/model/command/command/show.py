from library.model.command.base import Command


class Show(Command):
    name = "show"
    flag = ["no-color", "json"]
