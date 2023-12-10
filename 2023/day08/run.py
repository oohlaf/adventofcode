#!/usr/bin/env python3

from pathlib import Path
import re
import math


def parse_data(input):
    """Parse input data."""
    nodes = {}
    directions = ""
    for i, line in enumerate(input.splitlines()):
        if i == 0:
            directions = line.strip()
        if i > 1:
            data = re.findall(r"(\w{3}) = \((\w{3}), (\w{3})\)", line)
            nodes[data[0][0]] = (data[0][1], data[0][2])
    return directions, nodes


DIRECTION = {
    'L': 0,
    'R': 1
}


def star1(data):
    """Solve puzzle for star 1."""
    directions = data[0]
    nodes = data[1]
    n = "AAA"
    i = 0
    found = False
    while not found:
        for d in directions:
            i += 1
            n = nodes[n][DIRECTION[d]]
            if n == 'ZZZ':
                found = True
                break
    return i


def star2_slow(data):
    """Solve puzzle for star 2."""
    directions = data[0]
    nodes = data[1]
    pos = [n for n in nodes if n[2] == 'A']
    i = 0
    found = False
    while not found:
        for d in directions:
            i += 1
            z = 0
            for j, p in enumerate(pos):
                pos[j] = nodes[p][DIRECTION[d]]
                if pos[j][2] == 'Z':
                    z += 1
            if z == len(pos):
                found = True
                break
    return i


def find_z(start, directions, nodes):
    n = start
    i = 0
    found = False
    while not found:
        for d in directions:
            i += 1
            n = nodes[n][DIRECTION[d]]
            if n[2] == 'Z':
                found = True
                break
    return i


def star2(data):
    """Solve puzzle for star 2."""
    directions = data[0]
    nodes = data[1]
    steps = [find_z(n, directions, nodes) for n in nodes if n[2] == 'A']
    # find least common multiple for all path lengths to Z
    return math.lcm(*steps)


def solve(input):
    data = parse_data(input)
    yield star1(data)
    #yield star2_slow(data)
    yield star2(data)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())