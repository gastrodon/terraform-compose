from library.model.command.base import Command


class Init(Command):
    name = "init"
    kv = [
        "backend-config",
        "backend",
        "from-module",
        "ignore-remote-version",
        "input",
        "lock-timeout",
        "lock",
        "lockfile",
        "plugin-dir",
    ]
    flag = [
        "force-copy",
        "get",
        "migrate-state",
        "no-color",
        "reconfigure",
        "upgrade",
    ]
