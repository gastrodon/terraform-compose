from __future__ import annotations

PHASES: list[str] = [
    "planning",
    "applying",
]


DOTS_DOING: str = "..."
DOTS_OKAY: str = "  ✓"


class Status:
    def __init__(self, name: str):
        self.name = name
        self.done = False
        self.phase_index: int = 0

    @property
    def phase_count(self) -> int:
        return len(PHASES)

    def phase_next(self) -> Status:
        self.phase_index = (self.phase_index + 1 + self.phase_count) % self.phase_count
        return self

    def finish(self) -> Status:
        self.done = True
        return self

    @property
    def phase(self) -> str:
        return PHASES[self.phase_index]

    @property
    def dot(self) -> str:
        return DOTS_DOING if not self.done else DOTS_OKAY

    def render(self, lines: int) -> str:
        left: str = f"{self.phase} {self.name}"

        separator = " " * max(
            1,
            (lines - len(left) - len(self.dot)),
        )

        return f"{left}{separator}{self.dot}"
