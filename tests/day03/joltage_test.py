from unittest import TestCase
from aoc25.day03.__main__ import max_joltage1, max_joltage2


class JoltageTest(TestCase):
    def test_examples(self):
        banks = [
            ("987654321111111", 98),
            ("811111111111119", 89),
            ("234234234234278", 78),
            ("818181911112111", 92)
        ]
        for bank, expected in banks:
            with self.subTest(bank=bank):
                self.assertEqual(max_joltage1(bank), expected)

    def test_examples2(self):
        banks = [
            ("987654321111111", 987654321111),
            ("811111111111119", 811111111119),
            ("234234234234278", 434234234278),
            ("818181911112111", 888911112111)
        ]
        for bank, expected in banks:
            with self.subTest(bank=bank):
                self.assertEqual(max_joltage2(bank), expected)
