class Grid:
    def __init__(self, ascii_grid: str):
        self.grid = ascii_grid
        self._normalize_grid_end()

        self.width = self.grid.find("\n")
        self.height = len(self.grid) // (self.width + 1)

    def surrounding_rolls(self, x: int, y: int) -> int:
        self._assert_in_bounds(x, y)
        rolls = 0
        for cx in range(max(x - 1, 0), min(x + 2, self.width)):
            for cy in range(max(y - 1, 0), min(y + 2, self.height)):
                if (cx, cy) != (x, y) and self.get(cx, cy) == "@":
                    rolls += 1
        return rolls

    def get(self, x: int, y: int) -> str:
        self._assert_in_bounds(x, y)
        return self.grid[x + y * (self.width + 1)]

    def remove(self, x: int, y: int):
        self._assert_in_bounds(x, y)

        index = x + y * (self.width + 1)
        value = self.grid[index]
        if value != "@":
            raise ValueError(f"Cannot remove non-roll at ({x}, {y}): {value}")
        self.grid = self.grid[:index] + "x" + self.grid[index + 1:]

    def _assert_in_bounds(self, x: int, y: int):
        if not (0 <= x < self.width) or not (0 <= y < self.height):
            raise IndexError(f"Coordinates out of bounds: ({x}, {y})")

    def _normalize_grid_end(self):
        if self.grid[-2:] == "\n\n":
            self.grid = self.grid[:-1]
        elif self.grid[-1] != "\n":
            self.grid += "\n"

        if len(self.grid) % 2 != 0:
            raise ValueError("Grid len not even")
