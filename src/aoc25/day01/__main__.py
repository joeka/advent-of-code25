from pathlib import Path

from ..arguments import parse_args

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
    args = parse_args(day=1)
    main(args.input_file, args.part)
