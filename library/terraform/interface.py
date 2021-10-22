from typing import Any, Dict

from library.pretty.status import Status
from library.terraform import terraform


def do_up(name: str, config_set: Dict[str, Any]) -> (int, str, str):
    status = Status(name)
    print(status.render(0), end="\r")  # TODO get term length

    code, stdout, stderr = terraform.do_plan(
        config_set["plan"]["args"],
        config_set["plan"]["kwargs"],
    )

    if code:
        return code, stdout, stderr

    print(status.phase_next().render(0), end="\r")

    code, stdout, stderr = terraform.do_apply(
        config_set["apply"]["args"],
        config_set["apply"]["kwargs"],
    )

    print(status.finish().render(0))
    return code, stdout, stderr
