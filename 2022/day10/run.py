#!/usr/bin/env python3

from pathlib import Path


CPU_START_STATE = {"cycle": 1, "X": 1}


def ins_noop(state, value):
    state["cycle"] += 1
    yield state


def ins_addx(state, value):
    state["cycle"] += 1
    yield state
    state["X"] += value
    state["cycle"] += 1
    yield state


INSTRUCTIONS = {
    "noop": ins_noop,
    "addx": ins_addx,
}


def parse_data(input):
    """Parse input data."""
    result = [(line[0:4], int(line[5:])) if len(line) > 4 else (line[0:4], None) for line in input.split("\n")]
    return result


def print_status(state, ins):
    print(f"cycle: {state['cycle']}\tX: {state['X']}\tinstruction: {ins[0]} {ins[1]}")


def star1(data):
    """Solve puzzle for star 1."""
    cpu_state = CPU_START_STATE
    # print_status(cpu_state, (None, None))
    inspect = [20, 60, 100, 140, 180, 220]
    signal_strength = 0
    for ins in data:
        f = INSTRUCTIONS[ins[0]]
        for c in f(cpu_state, ins[1]):
            cpu_state = c
            if cpu_state['cycle'] in inspect:
                print_status(cpu_state, ins)
                signal_strength += cpu_state['cycle'] * cpu_state['X']
    return signal_strength


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
