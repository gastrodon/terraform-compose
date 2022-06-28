from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DependsNode:
    path: list[str] = field(default_factory=list)
    children: list[DependsNode] = field(default_factory=list)
