#!/usr/bin/env python3

from pathlib import Path


def parse_data(input):
    """Parse input data."""
    result = [[int(x) for x in line] for line in input.split("\n")]
    return result


def visible_left(x, y, data, w, h):
    for i in range(0, x):
        if data[y][i] >= data[y][x]:
            return 0
    return 1


def visible_right(x, y, data, w, h):
    for i in range(x + 1, w):
        if data[y][i] >= data[y][x]:
            return 0
    return 1


def visible_top(x, y, data, w, h):
    for j in range(0, y):
        if data[j][x] >= data[y][x]:
            return 0
    return 1


def visible_bottom(x, y, data, w, h):
    for j in range(y + 1, h):
        if data[j][x] >= data[y][x]:
            return 0
    return 1


def star1(data):
    """Solve puzzle for star 1."""
    w = len(data[0])
    h = len(data)
    visible = [[1 if (y == 0 or y == h - 1) or (x == 0 or x == w - 1) else 0 for x in range(w)] for y in range(h)]
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            visible[y][x] = (
                visible_left(x, y, data, w, h)
                or visible_right(x, y, data, w, h)
                or visible_top(x, y, data, w, h)
                or visible_bottom(x, y, data, w, h)
            )
    return sum(sum(visible, []))


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
