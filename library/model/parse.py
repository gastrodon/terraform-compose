from typing import Callable, Dict, List

Transform = Callable[[..., ..., Dict], Dict]


class Parse:
    _final: Transform = None
    _handle: List[Transform] = []

    def final(callable):
        if self._final:
            raise ValueError("@Parse.final has already been set")

        self._final = callable

    def handle(self, callable):
        self._handle += [callable]

    def parse(self, args: ..., compose: Dict) -> Dict:
        transformed = {**compose}

        for handle in self._handle:
            transformed = handle(args, transformed)

        return self._final(args, transformed) if self._final else transformed
