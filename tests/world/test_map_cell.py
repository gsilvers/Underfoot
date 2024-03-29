import unittest

from underfoot.world.map_cell import MapCell


class TestStringMethods(unittest.TestCase):
    def test_create_map_cell(self) -> None:
        """
        Quick test ensures able to create map cell and retrieve its contents
        """
        test_cell = MapCell(
            cell_position=(1, 1, 1),
            cell_terrain='MTN1',
            cell_objects_list=['PLY01', 'NPC01'],
        )
        assert test_cell.cell_position == (1, 1, 1)
        assert test_cell.cell_terrain == 'MTN1'
        assert test_cell.cell_objects_list == ['PLY01', 'NPC01']
        assert test_cell is not None

    def test_map_cell_populated(self) -> None:
        """
        Quick test is an object in the cell positive
        """
        test_cell = MapCell(
            cell_position=(1, 1, 1),
            cell_terrain='MTN1',
            cell_objects_list=['PLY01', 'NPC01'],
        )
        assert test_cell.cell_populated is True
