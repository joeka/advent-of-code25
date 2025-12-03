from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase
from aoc25.day01.__main__ import main


class Day01Test(TestCase):
    def test_part1(self):
        input_path = Path(__file__).parent / "test_input.txt"
        with redirect_stdout(StringIO()) as buffer:
            main(input_path)

        self.assertEqual(buffer.getvalue(), "3\n")

    def test_part2(self):
        input_path = Path(__file__).parent / "test_input.txt"
        with redirect_stdout(StringIO()) as buffer:
            main(input_path, part=2)

        self.assertEqual(buffer.getvalue(), "6\n")
