from typing import Any, Dict


def render_tree(tree: Dict[str, Any], level: int = 0) -> str:
    depends: list[Any] = tree.get("depends-on", [])

    return f"\n{'  '*level} | ".join(
        [tree["name"], *(render_tree(it, level + 1) for it in depends)]
    )
