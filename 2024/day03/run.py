#!/usr/bin/env python3

from pathlib import Path

import re


def parse_data(input):
    """Parse input data."""
    data = list()
    for line in input.splitlines():
        data.extend(re.findall(r"(mul|don't|do)\(((\d+),(\d+))?\)", line))
    return data


def star1(data):
    """Solve puzzle for star 1."""
    total = 0
    for op, arg, l, r in data:
        if op == 'mul':
            total += int(l) * int(r)
    return total


def star2(data):
    """Solve puzzle for star 2."""
    add = True
    total = 0
    for op, arg, l, r in data:
        if op == "don't":
            add = False
        elif op == 'do':
            add = True
        elif op == 'mul' and add:
            total += int(l) * int(r)
    return total


def solve(input):
    data = parse_data(input)
    yield star1(data)
    yield star2(data)


def main():
    # input_file = Path(__file__).parent / "sample.txt"
    # input_file = Path(__file__).parent / "sample2.txt"
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())