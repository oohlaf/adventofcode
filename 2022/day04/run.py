#!/usr/bin/env python3

from pathlib import Path


def parse_data(input):
    """Parse input data."""
    res = [[[int(x) for x in pair.split("-")] for pair in line.split(",")] for line in input.split("\n")]
    return res


def contained(pair):
    (x1, y1) = pair[0]
    (x2, y2) = pair[1]

    if x1 > y1:
        return False
    if x2 > y2:
        return False

    if x1 == x2 or y1 == y2:
        return True
    if x1 < x2 and y2 <= y1:
        return True
    if x1 > x2 and y1 <= y2:
        return True
    return False


def disjoint(pair):
    (x1, y1) = pair[0]
    (x2, y2) = pair[1]

    if x1 < x2 and y1 < x2:
        return True
    if x1 > y2 and y1 > y2:
        return True
    return False


def overlap(pair):
    (x1, y1) = pair[0]
    (x2, y2) = pair[1]

    if x1 <= x2 and y1 >= x2:
        return True
    if x1 <= y2 and y1 >= y2:
        return True
    if x2 <= x1 and y2 >= x1:
        return True
    if x2 <= y1 and y2 >= y1:
        return True
    return False


def star1(data):
    """Solve puzzle for star 1."""
    result = list(filter(contained, data))
    return len(result)


def star2(data):
    """Solve puzzle for star 2."""
    result = list(filter(overlap, data))
    return len(result)


def check_disjoint(data):
    """The disjoint set."""
    result = list(filter(disjoint, data))
    return len(result)


def solve(input):
    data = parse_data(input)
    yield star1(data)
    yield star2(data)
    # Should be 1000 with star2 answer
    yield check_disjoint(data)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())
