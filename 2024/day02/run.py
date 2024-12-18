#!/usr/bin/env python3

from pathlib import Path

import numpy as np


def parse_data(input):
    """Parse input data."""
    data = list()
    for line in input.splitlines():
        row = np.fromstring(line, dtype=int, sep=' ')
        data.append(row)
    return np.array(data, dtype=object)


def is_safe(report):
    diff = np.diff(report)
    is_inc = (diff > 0) == (diff < 4)
    is_dec = (diff < 0) == (diff > -4)
    if np.all(is_inc):
        return 1
    if np.all(is_dec):
        return 1
    return 0


def dampener(report):
    if is_safe(report):
        return 1
    for i in range(report.size):
        arr = np.delete(report, i)
        if is_safe(arr):
            return 1
    return 0


def star1(data):
    """Solve puzzle for star 1."""
    return np.sum([is_safe(report) for report in data])


def star2(data):
    """Solve puzzle for star 2."""
    return np.sum([dampener(report) for report in data])


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