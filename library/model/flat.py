from typing import List, Tuple, TypeVar, Union

FlatPath = List[Union[str, int]]
FlatItem = TypeVar("FlatItem", int, float, str, None)
FlatEntries = Tuple[FlatPath, FlatItem]
