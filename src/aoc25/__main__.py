from pathlib import Path
from importlib import import_module

from .arguments import parse_args


def main(input_file: Path, day: int, part: int = 1) -> None:
    import_module(f".day{day:02d}.__main__", "aoc25").main(input_file, part)


if __name__ == "__main__":
    args = parse_args()
    main(args.input_file, args.day, args.part)
