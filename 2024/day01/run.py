#!/usr/bin/env python3

from pathlib import Path

import numpy


def parse_data(input):
    """Parse input data."""
    group1 = []
    group2 = []
    for line in input.splitlines():
        data = line.split()
        group1.append(int(data[0]))
        group2.append(int(data[1]))
    group1.sort()
    group2.sort()
    return (group1, group2)


def star1(data):
    """Solve puzzle for star 1."""
    total = 0
    for i, j in zip(data[0], data[1]):
        d = abs(j - i)
        total += d
    return total


def star2(data):
    """Solve puzzle for star 2."""
    unique, counts = numpy.unique(data[1], return_counts=True)
    occurances = dict(zip(unique, counts))
    total = 0
    for i in data[0]:
        if i in occurances:
            total += i * occurances[i]
    return total


def solve(input):
    data = parse_data(input)
    yield star1(data)
    yield star2(data)


def main():
    # input_file = Path(__file__).parent / "sample.txt"
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())