from pathlib import Path

from ..arguments import parse_args


def main(input_file: Path, part: int = 1):
    pass


if __name__ == "__main__":
    args = parse_args(day=1)
    main(args.input_file, args.part)
