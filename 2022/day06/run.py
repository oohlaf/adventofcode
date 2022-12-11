#!/usr/bin/env python3

from pathlib import Path


def parse_data(input):
    """Parse input data."""
    return [line for line in input.split("\n")]


def is_marker(data):
    return len(data) == len(set(data))


def process(data):
    buffer = []
    i = 0
    for x in data:
        i += 1
        if i > 4:
            buffer.pop(0)
        if i > 3:
            buffer.append(x)
            if is_marker(buffer):
                return i
        else:
            buffer.append(x)
    raise ValueError


def star1(data):
    """Solve puzzle for star 1."""
    line_positions = []
    for line in data:
        pos = process(line)
        line_positions.append(pos)
    return line_positions


def star2(data):
    """Solve puzzle for star 2."""


def solve(input):
    data = parse_data(input)
    yield star1(data)
    yield star2(data)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())