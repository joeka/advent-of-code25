from unittest import TestCase
from aoc25.day01.dial import Dial


class DialTest(TestCase):
    def test_reset(self):
        dial = Dial()
        dial.turn("R30")
        dial.reset()
        self.assertEqual(dial.position, 50)
        self.assertEqual(dial.hit_zero, 0)

    def test_turn_right(self):
        dial = Dial()
        dial.turn("R10")
        self.assertEqual(dial.position, 60)
        self.assertEqual(dial.hit_zero, 0)

    def test_turn_left(self):
        dial = Dial()
        dial.turn("L20")
        self.assertEqual(dial.position, 30)

    def test_wrap_around_right(self):
        dial = Dial()
        dial.turn("R50")
        self.assertEqual(dial.position, 0)
        self.assertEqual(dial.hit_zero, 1)
        self.assertEqual(dial.passed_zero, 1)

    def test_wrap_around_left(self):
        dial = Dial()
        dial.turn("L51")
        self.assertEqual(dial.position, 99)
        self.assertEqual(dial.hit_zero, 0)
        self.assertEqual(dial.passed_zero, 1)

    def test_multiple_turns(self):
        dial = Dial()
        dial.turn("R160")
        self.assertEqual(dial.position, 10)
        self.assertEqual(dial.hit_zero, 0)
        self.assertEqual(dial.passed_zero, 2)

        dial.turn("L220")
        self.assertEqual(dial.position, 90)
        self.assertEqual(dial.hit_zero, 0)
        self.assertEqual(dial.passed_zero, 5)

    def test_example(self):
        dial = Dial()
        dial.turn("R1000")

        self.assertEqual(dial.position, 50)
        self.assertEqual(dial.passed_zero, 10)

    def test_zero_to_zero(self):
        dial = Dial()
        dial.turn("R50")
        self.assertEqual(dial.position, 0)
        self.assertEqual(dial.passed_zero, 1)

        dial.turn("L100")
        self.assertEqual(dial.position, 0)
        self.assertEqual(dial.passed_zero, 2)

    def test_directly_hit_zero(self):
        dial = Dial()
        dial.turn("L50")
        self.assertEqual(dial.position, 0)
        self.assertEqual(dial.hit_zero, 1)
        self.assertEqual(dial.passed_zero, 1)

    def test_left_from_zero(self):
        dial = Dial()
        dial.turn("L50")
        dial.turn("L50")

        self.assertEqual(dial.position, 50)
        self.assertEqual(dial.hit_zero, 1)
        self.assertEqual(dial.passed_zero, 1)

    def test_edge_cases(self):
        cases = [
            ("R100", 0, 1),
            ("L100", 0, 1),
            ("L100", 1, 1),
            ("R100", 1, 1),
            ("L101", 1, 2),
        ]
        for instruction, initial, expected in cases:
            with self.subTest(instruction=instruction, initial=initial,
                              expected=expected):
                dial = Dial()
                dial.position = initial
                dial.turn(instruction)
                self.assertEqual(dial.passed_zero, expected)
