from pathlib import Path

from ..arguments import parse_args


def part2(input_file: Path):
    timelines = 0
    beams = {}
    with input_file.open() as file:
        for line in file:
            if not beams:
                beams[line.find("S")] = 1
                timelines = 1
                continue

            for beam, count in beams.copy().items():
                if line[beam] == "^":
                    left = beam - 1
                    right = beam + 1
                    if left not in beams:
                        beams[left] = count
                    else:
                        beams[left] += count
                    if right not in beams:
                        beams[right] = count
                    else:
                        beams[right] += count

                    timelines += count
                    del beams[beam]

    print(timelines)


def part1(input_file: Path):
    split_count = 0
    beams = set()
    with input_file.open() as file:
        for line in file:
            if not beams:
                beams.add(line.find("S"))
                continue

            for beam in beams.copy():
                if line[beam] == "^":
                    split_count += 1
                    beams.remove(beam)
                    beams.add(beam - 1)
                    beams.add(beam + 1)

    print(split_count)


def main(input_file: Path, part: int = 1):
    if part == 1:
        part1(input_file)
    else:
        part2(input_file)


if __name__ == "__main__":
    args = parse_args(day=7)
    main(args.input_file, args.part)
