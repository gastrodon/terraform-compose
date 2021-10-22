import json
from multiprocessing import Pool
from typing import Any, Dict, List

import app
from library import config, terraform
from library.config.defaults import OUTPUT
from library.types import options
from library.types.kind import Kind


def output_wrapped(config: Dict[str, Any]) -> Dict[str, Any]:
    ran = terraform.do(Kind.output, config["args"], config["kwargs"])

    if ran[0]:
        raise Exception(ran[2])

    return {config["name"]: json.loads(ran[1])}


@app.app.command(name="output")
def handle_output(
    services: List[str] = options.services,
    file: str = options.file,
):
    compose = config.read_file(file)
    configs = [
        {
            "name": service,
            "args": [],
            "kwargs": config.read(OUTPUT, service, compose),
        }
        for service in services or compose["services"].keys()
    ]

    with Pool(processes=len(configs)) as pool:
        results = {
            key: value
            for result in pool.map(output_wrapped, configs)
            for key, value in result.items()
        }

    print(json.dumps(results, indent=2, sort_keys=True))
