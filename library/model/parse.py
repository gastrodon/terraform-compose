from typing import Callable, Dict, List

Transform = Callable[[..., ..., Dict], Dict]


class Parse:
    _final: Transform = None
    _final_set: bool = False
    _handle: List[Transform] = []

    def final(callable):
        if self._final_set:
            raise ValueError("@Parse.final has already been set")

        self._final_set = True
        self._final = callable

    def handle(self, callable):
        self._handle += [callable]

    def parse(self, command: ..., args: ..., compose: Dict) -> Dict:
        transformed = {**compose}

        for handle in self._handle:
            transformed = handle(command, args, transformed)

        if self._final_set:
            return self._final(command, args, transformed)

        return transformed
