#!/usr/bin/env python3

from pathlib import Path


def parse_data(input):
    """Parse input data."""
    return [line for line in input.split("\n")]


def is_marker(data):
    return len(data) == len(set(data))


def process_packet(state, x):
    if len(state["sop"]) == 4:
        state["sop"].pop(0)
        state["sop"].append(x)
        return is_marker(state["sop"])
    state["sop"].append(x)
    return False


def process_message(state, x):
    if len(state["som"]) == 14:
        state["som"].pop(0)
        state["som"].append(x)
        return is_marker(state["som"])
    state["som"].append(x)
    return False


def process(data, detect="sop"):
    state = {
        "sop": [],
        "som": [],
    }

    i = 0
    for x in data:
        i += 1
        if process_packet(state, x):
            if detect == "sop":
                return i
        if process_message(state, x):
            if detect == "som":
                return i
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
    line_positions = []
    for line in data:
        pos = process(line, detect="som")
        line_positions.append(pos)
    return line_positions


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
