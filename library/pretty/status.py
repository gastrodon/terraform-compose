from __future__ import annotations

PHASES: list[str] = [
    "planning",
    "applying",
]


DOTS_DOING: str = "..."
DOTS_DONE: str = "done"
DOTS_SKIP: str = "skip"


class Status:
    def __init__(self, name: str, phases: list[str] = PHASES):
        self.name: str = name
        self.phases: list[str] = phases

        self.done: bool = False
        self.skiped: bool = False
        self.phase_index: int = 0

    @property
    def phase_count(self) -> int:
        return len(self.phases)

    def phase_next(self) -> Status:
        self.phase_index = (self.phase_index + 1 + self.phase_count) % self.phase_count
        return self

    def finish(self) -> Status:
        self.done = True
        return self

    def skip(self) -> Status:
        self.skiped = True
        return self

    @property
    def phase(self) -> str:
        return self.phases[self.phase_index]

    @property
    def dot(self) -> str:
        if self.skiped:
            return DOTS_SKIP

        if self.done:
            return DOTS_DONE

        return DOTS_DOING

    def render(self, lines: int) -> str:
        left: str = f"{self.phase} {self.name}"

        separator = " " * max(
            1,
            (lines - len(left) - len(self.dot)),
        )

        return f"{left}{separator}{self.dot}"
