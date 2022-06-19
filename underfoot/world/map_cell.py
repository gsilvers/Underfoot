from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class MapCell:
    """
    Class representing a single cell on our 2d map
    Our map will be a mesh of these. We will only display in 2d
    But through doors etc additional cells may be above or below current
    """

    cell_position: Tuple[int, int, int]
    cell_terrain: str
    cell_objects_list: List[str]
