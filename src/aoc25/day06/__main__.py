import io
from pathlib import Path
import pandas as pd
from math import prod

from ..arguments import parse_args


def part2(input_file: Path):
    total = 0
    with input_file.open() as file:
        width = len(file.readline())
        file.seek(0, io.SEEK_END)
        eof = file.tell()
        height = round((eof + 1) / width)

        current = 0
        values = []
        for column in range(width - 2, -1, -1):
            for row in range(0, height):
                file.seek(column + row * width)
                char = file.read(1)
                match char:
                    case ' ':
                        continue
                    case '+':
                        values.append(current)
                        total += sum(values)
                        values.clear()
                        current = 0
                    case '*':
                        values.append(current)
                        total += prod(values)
                        values.clear()
                        current = 0
                    case _:
                        current *= 10
                        current += int(char)
            if current > 0:
                values.append(current)
                current = 0

    print(total)


def part1(input_file: Path):
    df = pd.read_csv(input_file, sep="\\s+", header=None)
    sum = 0
    for column in df:
        series = df[column]
        operator = series.pop(series.last_valid_index())
        series = series.astype("int64")
        if operator == '+':
            sum += int(series.sum())
        elif operator == '*':
            sum += int(series.product())

    print(sum)


def main(input_file: Path, part: int = 1):
    if part == 1:
        part1(input_file)
    else:
        part2(input_file)


if __name__ == "__main__":
    args = parse_args(day=6)
    main(args.input_file, args.part)
