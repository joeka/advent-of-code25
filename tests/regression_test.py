from unittest import TestCase
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json

from aoc25.day01.__main__ import main


class RegressionTests(TestCase):
    def setUp(self):
        answers_path = Path(__file__).parent.parent / "answers.json"
        with answers_path.open() as answers_file:
            self.answers = json.load(answers_file)

    def test_day01_part1(self):
        input_path = Path(__file__).parent.parent / "inputs" / "day01.txt"
        with redirect_stdout(StringIO()) as buffer:
            main(input_path)

        self.assertEqual(buffer.getvalue(), f"{self.answers["day01part1"]}\n")

    def test_day01_part2(self):
        input_path = Path(__file__).parent.parent / "inputs" / "day01.txt"
        with redirect_stdout(StringIO()) as buffer:
            main(input_path, part=2)

        self.assertEqual(buffer.getvalue(), f"{self.answers["day01part2"]}\n")
