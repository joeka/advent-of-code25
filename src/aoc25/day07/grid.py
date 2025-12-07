START = ord("S")
SPLIT = ord("^")
EMPTY = ord(".")


class Grid:
    def __init__(self, ascii_grid: str):
        self.width = ascii_grid.find("\n")
        self.grid = bytearray(ascii_grid.replace(
            "\n", "").strip().encode("utf-8"))

        self.height = len(self.grid) // (self.width)

    def get(self, x: int, y: int) -> int:
        return self.grid[x + y * self.width]
