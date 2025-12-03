from argparse import ArgumentParser
from pathlib import Path

from .dial import Dial


def main(input_file: Path, part: int = 1) -> None:
    dial = Dial()
    with input_file.open("r") as f:
        for line in f:
            dial.turn(line)
    if part == 1:
        print(dial.hit_zero)
    else:
        print(dial.passed_zero)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input_file", type=Path)
    parser.add_argument("--part", type=int, default=1, choices=[1, 2])
    args = parser.parse_args()
    main(args.input_file, args.part)
