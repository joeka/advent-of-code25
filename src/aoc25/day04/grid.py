ROLL = ord("@")
EMPTY = ord(".")
REMOVED = ord("x")


class Grid:
    def __init__(self, ascii_grid: str):
        self.width = ascii_grid.find("\n")
        self.grid = bytearray(ascii_grid.replace(
            "\n", "").strip().encode("utf-8"))

        self.height = len(self.grid) // (self.width)

    def surrounding_rolls(self, x: int, y: int) -> int:
        self._assert_in_bounds(x, y)
        rolls = 0
        for cx in range(max(x - 1, 0), min(x + 2, self.width)):
            for cy in range(max(y - 1, 0), min(y + 2, self.height)):
                if (cx, cy) != (x, y) and self.get(cx, cy) == ROLL:
                    rolls += 1
        return rolls

    def get(self, x: int, y: int) -> int:
        self._assert_in_bounds(x, y)
        return self.grid[x + y * self.width]

    def remove(self, x: int, y: int):
        self._assert_in_bounds(x, y)

        index = x + y * self.width
        value = self.grid[index]
        if value != ROLL:
            raise ValueError(
                f"Cannot remove non-roll at ({x}, {y}): {chr(value)}")
        self.grid[index] = REMOVED

    def _assert_in_bounds(self, x: int, y: int):
        if not (0 <= x < self.width) or not (0 <= y < self.height):
            raise IndexError(f"Coordinates out of bounds: ({x}, {y})")
