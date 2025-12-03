from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Optional


def parse_args(day: Optional[int] = None) -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("input_file", type=Path)
    if day is None:
        parser.add_argument("--day", type=int, choices=range(1, 13))
    parser.add_argument("--part", type=int, default=1, choices=[1, 2])
    return parser.parse_args()
