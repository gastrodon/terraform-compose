from __future__ import annotations

PHASES: list[str] = [
    "planning",
    "applying",
]

DOTS: list[str] = [
    ".  ",
    " . ",
    "  .",
    " . ",
]

DOTS_DONE: str = "..."


class Animation:
    def __init__(self, name: str):
        self.name = name
        self.done = False
        self.phase_index: int = 0
        self.dot_index: int = 0

    @property
    def phase_count(self) -> int:
        return len(PHASES)

    @property
    def dot_count(self) -> int:
        return len(DOTS)

    @property
    def phase_next(self) -> Animation:
        self.phase_index = (self.phase_index + 1 + self.phase_count) % self.phase_count
        return self

    @property
    def dot_next(self) -> Animation:
        self.dot_index = (self.dot_index + 1 + self.dot_count) % self.dot_count
        return self

    @property
    def phase(self) -> str:
        return PHASES[self.phase_index]

    @property
    def dot(self) -> str:
        return DOTS_DONE if self.dot_index == -1 else DOTS[self.dot_index]

    @property
    def finished(self) -> Animation:
        self.dot_index = -1
        return self

    def render(self, lines: int) -> str:
        left: str = f"{self.phase} {self.name}"

        separator = " " * max(
            1,
            (lines - len(left) - len(self.dot)),
        )

        return f"{left}{separator}{self.dot}"
