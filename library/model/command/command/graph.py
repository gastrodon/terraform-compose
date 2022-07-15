from library.model.command.base import Command


class Graph(Command):
    name = "graph"
    flag = ["groups", "no-color", "json"]
