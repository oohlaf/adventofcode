#!/usr/bin/env python3

from pathlib import Path
from io import StringIO
import numpy as np


def parse_data(input):
    """Parse input data."""
    w = len(input.splitlines()[0])
    conv = lambda x: int(1) if x == b'#' else int(0)
    data = np.genfromtxt(StringIO(input), dtype=int, delimiter=1, comments=None, converters={i: conv for i in range(w)})
    return data


def distance(a, b):
    ay, ax = a
    by, bx = b
    dy = abs(by - ay)
    dx = abs(bx - ax)
    return dy + dx


def star1(data):
    """Solve puzzle for star 1."""
    zero_cols = np.nonzero(~data.any(axis=0))[0]
    zero_rows = np.nonzero(~data.any(axis=1))[0]
    # expand the universe
    universe = np.insert(data, zero_cols, 0, axis=1)
    universe = np.insert(universe, zero_rows, 0, axis=0)
    galaxies = {}
    y, x = np.nonzero(universe)
    for i, coord in enumerate(list(zip(y, x))):
        galaxies[i] = coord
    #print(galaxies)
    num = len(galaxies)
    total = 0
    for i in galaxies:
        for j in range(i+1, num):
            d = distance(galaxies[i], galaxies[j])
            #print(galaxies[i], galaxies[j], d)
            total += d
    return total


def distance2(a, b, zero_cols, zero_rows, m):
    ay, ax = a
    by, bx = b
    col_path = np.zeros(zero_cols.shape, dtype=int)
    row_path = np.zeros(zero_rows.shape, dtype=int)
    for i in range(min(ax,bx), max(ax,bx)):
        col_path[i] = 1
    for i in range(min(ay,by), max(ay,by)):
        row_path[i] = 1
    dx_exp = np.sum(zero_cols * col_path)
    dy_exp = np.sum(zero_rows * row_path)
    dx = abs(bx - ax) + dx_exp * (m-1)
    dy = abs(by - ay) + dy_exp * (m-1)
    return dy + dx


def star2(data):
    """Solve puzzle for star 2."""
    zero_cols = 1*(data == 0).all(axis=0)
    zero_rows = 1*(data == 0).all(axis=1)
    galaxies = {}
    y, x = np.nonzero(data)
    for i, coord in enumerate(list(zip(y, x))):
        galaxies[i] = coord
    num = len(galaxies)
    total = 0
    for i in galaxies:
        for j in range(i+1, num):
            d = distance2(galaxies[i], galaxies[j], zero_cols, zero_rows, 1000000)
            #print(galaxies[i], galaxies[j], d)
            total += d
    return total


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