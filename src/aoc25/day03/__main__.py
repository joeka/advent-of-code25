from pathlib import Path

from ..arguments import parse_args


class Battery:
    def __init__(self, position: int, joltage: int):
        self.position = position
        self.joltage = joltage

    def __ge__(self, other: "Battery") -> bool:
        return self.joltage >= other.joltage


def max_joltage1(bank: str) -> int:
    max_joltage = int(bank[-2])
    not_quite_max = int(bank[-1])
    for battery in reversed(bank[:-2]):
        joltage = int(battery)
        if joltage >= max_joltage:
            if max_joltage > not_quite_max:
                not_quite_max = max_joltage
            max_joltage = joltage
    return max_joltage * 10 + not_quite_max


def max_joltage2(bank: str, limit=12) -> int:
    batteries = [Battery(pos, int(joltage))
                 for pos, joltage in enumerate(bank)]

    max_joltages = []
    left_limit = 0
    for i in range(-limit, 0):
        max_joltage = batteries[i]
        for battery in reversed(batteries[left_limit:i]):
            if battery >= max_joltage:
                max_joltage = battery
        max_joltages.append(max_joltage)
        left_limit = max_joltage.position + 1

    result = 0
    for i, battery in enumerate(reversed(max_joltages)):
        result += battery.joltage * (10 ** i)
    return result


def main(input_file: Path, part: int = 1):
    max_joltage = max_joltage1 if part == 1 else max_joltage2

    sum_of_all_joltage = 0
    with input_file.open("r") as file:
        for bank in file:
            sum_of_all_joltage += max_joltage(bank.strip())

    print(sum_of_all_joltage)


if __name__ == "__main__":
    args = parse_args(day=3)
    main(args.input_file, args.part)
