from math import log, floor


def validate_range(start: int, end: int) -> int:
    digit_count = digits(start)
    if not even(digit_count):
        half = int(10 ** ((digit_count - 1) / 2))
        digit_count += 1
    else:
        factor = 10 ** (digit_count / 2)
        high = int(start / factor)
        low = int(start % factor)
        half = high if high >= low else high + 1

    sum = 0

    digit_count = int(digit_count / 2)
    while True:
        total = mirror(half, digit_count)
        if total > end:
            return sum
        sum += total
        half += 1
        digit_count = digits(half)


def mirror(number: int, digit_count: int) -> int:
    return int(number * (10 ** digit_count)) + number


def even(number: int) -> bool:
    return number % 2 == 0


def digits(number: int) -> int:
    return floor(log(number, 10)) + 1
