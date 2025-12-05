from pathlib import Path
from enum import Enum, auto

from ..arguments import parse_args


class Mode(Enum):
    RANGES = auto()
    VALUES = auto()


def part2(ranges: list[list[int]]):
    sum = 0
    for r in ranges:
        sum += r[1] - r[0] + 1
    print(sum)


def part1(ranges: list[list[int]], values: list[int]):
    fresh = 0
    for value in values:
        if in_any(value, ranges):
            fresh += 1

    print(fresh)


def in_any(value, ranges) -> bool:
    for r in ranges:
        if r[0] <= value <= r[1]:
            return True
    return False


def main(input_file: Path, part: int = 1):
    mode = Mode.RANGES
    ranges = []
    values = []
    with input_file.open() as file:
        for line in file:
            line = line.strip()
            if mode == Mode.RANGES:
                if line == "":
                    if part == 1:
                        mode = Mode.VALUES
                        continue
                    else:
                        break

                start, end = map(int, line.split("-"))
                ranges.append([start, end])
            else:
                if line == "":
                    break

                values.append(int(line))

    ranges.sort(key=lambda r: r[0])
    merged_ranges = []
    for r in ranges:
        if not merged_ranges:
            merged_ranges.append(r)
        else:
            previous = merged_ranges[-1]
            if r[0] > previous[1]:
                merged_ranges.append(r)
            else:
                previous[1] = max(r[1], previous[1])

    if part == 1:
        part1(merged_ranges, values)
    else:
        part2(merged_ranges)


if __name__ == "__main__":
    args = parse_args(day=5)
    main(args.input_file, args.part)
