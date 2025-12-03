from pathlib import Path

from ..arguments import parse_args

from .validation import validate_range


def main(input_file: Path, part: int = 1):
    ranges = [text.split('-')
              for text in input_file.read_text().strip().split(',')]
    result = 0
    for range in ranges:
        result += validate_range(int(range[0]), int(range[1]))

    print(result)


if __name__ == "__main__":
    args = parse_args(day=1)
    main(args.input_file, args.part)
