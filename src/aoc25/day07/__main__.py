from pathlib import Path

from ..arguments import parse_args


def add(beams: dict[int, int], pos: int, count: int):
    if pos not in beams:
        beams[pos] = count
    else:
        beams[pos] += count


def main(input_file: Path, part: int = 1):
    split_count = 0
    timelines = 0
    beams = {}
    with input_file.open() as file:
        for line in file:
            if not beams:
                beams[line.find("S")] = 1
                timelines = 1
                next(file)  # skip 1
                continue

            for beam, count in beams.copy().items():
                if line[beam] == "^":
                    split_count += 1

                    add(beams, beam - 1, count)
                    add(beams, beam + 1, count)

                    timelines += count
                    del beams[beam]

            next(file)  # skip 1

    if part == 1:
        print(split_count)
    else:
        print(timelines)


if __name__ == "__main__":
    args = parse_args(day=7)
    main(args.input_file, args.part)
