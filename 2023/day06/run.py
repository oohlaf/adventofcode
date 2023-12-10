#!/usr/bin/env python3

from pathlib import Path
import re
import numpy as np
from math import prod
from numpy.polynomial import Polynomial


def parse_data(input):
    """Parse input data."""
    time = []
    distance = []
    for line in input.splitlines():
        data = line.split(":")
        if data[0] == "Time":
            time = [int(t) for t in data[1].split()]
        elif data[0] == "Distance":
            distance = [int(t) for t in data[1].split()]
    return time, distance


def parse_data2(input):
    """Parse input data."""
    time = []
    distance = []
    for line in input.splitlines():
        data = line.split(":")
        if data[0] == "Time":
            time = int("".join(data[1].split()))
        elif data[0] == "Distance":
            distance = int("".join(data[1].split()))
    return time, distance


# d(x) = -x^2 + t*x
# 0 = -1*x^2 + t*x - d
def ways(t, d):
    p = Polynomial([-d, t, -1])
    r = p.roots().astype(int)
    d = np.diff(r)
    if t % 2 == d % 2:
        d -= 1
    return d.item()


def star1(data):
    """Solve puzzle for star 1."""
    time = data[0]
    dist = data[1]
    return prod(map(ways, time, dist))


def star2(data):
    """Solve puzzle for star 2."""
    time = data[0]
    dist = data[1]
    return ways(time, dist)


def solve(input):
    data = parse_data(input)
    yield star1(data)
    data = parse_data2(input)
    yield star2(data)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())