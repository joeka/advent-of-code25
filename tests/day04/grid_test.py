from unittest import TestCase
from aoc25.day04.grid import Grid


class GridTest(TestCase):
    def test_grid_initialization_no_trailing_newline(self):
        ascii_grid = "...\n...\n..."
        grid = Grid(ascii_grid)
        self.assertEqual(grid.width, 3)
        self.assertEqual(grid.height, 3)
        self.assertEqual(grid.grid, ascii_grid + "\n")

    def test_grid_initialization_with_trailing_newline(self):
        ascii_grid = "....\n....\n"
        grid = Grid(ascii_grid)
        self.assertEqual(grid.width, 4)
        self.assertEqual(grid.height, 2)
        self.assertEqual(grid.grid, ascii_grid)

    def test_grid_initialization_with_double_trailing_newline(self):
        ascii_grid = "..\n..\n\n"
        grid = Grid(ascii_grid)
        self.assertEqual(grid.width, 2)
        self.assertEqual(grid.height, 2)
        self.assertEqual(grid.grid, "..\n..\n")

    def test_get(self):
        ascii_grid = "..\n.@\n"
        grid = Grid(ascii_grid)
        self.assertEqual(grid.get(0, 1), ".")
        self.assertEqual(grid.get(1, 0), ".")
        self.assertEqual(grid.get(1, 1), "@")

    def test_surrounding_rolls(self):
        ascii_grid = "...\n.@.\n..."
        grid = Grid(ascii_grid)
        self.assertEqual(grid.surrounding_rolls(1, 1), 0)

        ascii_grid = (
            "@@.\n"
            "@@.\n"
            "..@\n"
        )
        grid = Grid(ascii_grid)
        self.assertEqual(grid.surrounding_rolls(0, 0), 3)
        self.assertEqual(grid.surrounding_rolls(1, 1), 4)
        self.assertEqual(grid.surrounding_rolls(2, 2), 1)
