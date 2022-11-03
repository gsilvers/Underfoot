#!/usr/bin/env python3
"""
This module represents the current 32x18 panel visible to the player
"""

from underfoot.world.map_cell import MapCell

VISIBLE_ROWS = 18
VISIBLE_COLUMNS = 32


class ActiveViewer:
    map_tiles: 'list[list[MapCell]]' = [[]]

    def __init__(self) -> None:
        self.map_tiles = [
            [
                MapCell(cell_position=(i, j, 0), cell_terrain='DFLT', cell_objects_list=[])
                for i in range(VISIBLE_COLUMNS)
            ]
            for j in range(VISIBLE_ROWS)
        ]

    def dump_map(self) -> None:
        print(self.map_tiles)
