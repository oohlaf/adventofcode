#!/usr/bin/env python3

import string

from pathlib import Path


def build_prio_dict():
    prio_dict = {}
    for i in range(len(string.ascii_letters)):
        prio_dict[string.ascii_letters[i]] = i + 1
    return prio_dict


PRIO_DICT = build_prio_dict()


def get_prio(item):
    return PRIO_DICT[item]


def process_compartment_input(input):
    for line in input.split("\n"):
        if len(line) % 2:
            raise ValueError
        middle = len(line) // 2
        yield (line[:middle], line[middle:])


def parse_compartment_data(input):
    """Parse input data per rugsack compartment."""
    return list(process_compartment_input(input))


def parse_group_data(input):
    """Parse input data per group of elfs."""
    all_groups = []
    cur_group = []
    for line in input.split("\n"):
        if len(cur_group) >= 3:
            all_groups.append(cur_group)
            cur_group = []
        cur_group.append(line)
    if len(cur_group):
        all_groups.append(cur_group)
    return all_groups


def intersection(a, b):
    return [value for value in a if value in b]


def star1(data):
    """Solve puzzle for star 1."""
    total_prio = 0
    for bag in data:
        comp_one, comp_two = bag
        common_set = set(intersection(comp_one, comp_two))
        prio = sum(map(get_prio, common_set))
        total_prio += prio
    return total_prio


def star2(data):
    """Solve puzzle for star 2."""
    total_prio = 0
    for group in data:
        common_set = intersection(intersection(set(group[0]), set(group[1])), set(group[2]))
        prio = sum(map(get_prio, common_set))
        total_prio += prio
    return total_prio


def solve(input):
    data = parse_compartment_data(input)
    yield star1(data)
    data = parse_group_data(input)
    yield star2(data)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())
