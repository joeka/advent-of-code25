from unittest import TestCase
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json

from aoc25.__main__ import main


class RegressionTests(TestCase):
    def test_regressions(self):
        answers_path = Path(__file__).parent.parent / "answers.json"
        with answers_path.open() as answers_file:
            answers = json.load(answers_file)

        for key, expected in answers.items():
            day = int(key[3:5])
            part = int(key[-1:])
            with self.subTest(day=day, part=part):
                input_path = Path(__file__).parent.parent / \
                    "inputs" / f"day{day:02d}.txt"

                with redirect_stdout(StringIO()) as buffer:
                    main(input_path, day=day, part=part)

                self.assertEqual(int(buffer.getvalue().strip()), expected)
