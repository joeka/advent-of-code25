from pathlib import Path

from ..arguments import parse_args

from .grid import Grid, ROLL


def main(input_file: Path, part: int = 1):
    grid = Grid(input_file.read_text())
    sum = 0
    removed = 0
    while True:
        for x in range(grid.width):
            for y in range(grid.height):
                if grid.get(x, y) == ROLL and grid.surrounding_rolls(x, y) < 4:
                    if part == 2:
                        grid.remove(x, y)
                        removed += 1
                    sum += 1

        if removed == 0:
            print(sum)
            return
        removed = 0


if __name__ == "__main__":
    args = parse_args(day=4)
    main(args.input_file, args.part)
