#!/usr/bin/env python3

import string

from pathlib import Path


def build_prio_dict():
    prio_dict = {}
    for i in range(len(string.ascii_letters)):
        prio_dict[string.ascii_letters[i]] = i + 1
    return prio_dict


def process_input(input):
    for line in input.split("\n"):
        if len(line) % 2:
            raise ValueError
        middle = len(line) // 2
        yield (line[:middle], line[middle:])


def parse_data(input):
    """Parse input data."""
    return list(process_input(input))


def intersection(a, b):
    return [value for value in a if value in b]


def star1(data):
    """Solve puzzle for star 1."""
    prio_dict = build_prio_dict()

    def get_prio(item):
        return prio_dict[item]

    total_prio = 0
    for bag in data:
        comp_one, comp_two = bag
        common_set = set(intersection(comp_one, comp_two))
        prio = sum(map(get_prio, common_set))
        total_prio += prio
    return total_prio


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
