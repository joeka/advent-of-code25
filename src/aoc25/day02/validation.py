from math import log, floor
import re


INVALID_PATTERN = re.compile("^(.+)\\1+$")


def validate_range2(start: int, end: int) -> int:
    invalid_sum = 0
    for id in range(start, end + 1):
        if INVALID_PATTERN.match(str(id)):
            invalid_sum += id

    return invalid_sum


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

    invalid_sum = 0

    digit_count = int(digit_count / 2)
    while True:
        total = mirror(half, digit_count)
        if total > end:
            return invalid_sum
        invalid_sum += total
        half += 1
        digit_count = digits(half)


def mirror(number: int, digit_count: int) -> int:
    return int(number * (10 ** digit_count)) + number


def even(number: int) -> bool:
    return number % 2 == 0


def digits(number: int) -> int:
    return floor(log(number, 10)) + 1
