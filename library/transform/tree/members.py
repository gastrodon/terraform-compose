from typing import Dict, Set


def members(name: str, services: Dict) -> Set[str]:
    return {
        name,
        *services[name]["depends-on"],
        *{
            member
            for sub_name in services[name]["depends-on"]
            for member in members(sub_name, services)
        },
    }
