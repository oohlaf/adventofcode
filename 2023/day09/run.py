#!/usr/bin/env python3

from pathlib import Path


def parse_data(input):
    """Parse input data."""
    data = []
    for line in input.splitlines():
        seq = [int(n) for n in line.split()]
        data.append(seq)
    return data


def row_diff(seq):
    return [seq[i+1] - seq[i] for i in range(len(seq) - 1)]


def star1(data):
    """Solve puzzle for star 1."""
    total = 0
    for row in data:
        print("row", row)
        steps = [row]
        step = row
        while any(v != 0 for v in step):
            step = row_diff(step)
            steps.append(step)
        val = sum([seq[-1] for seq in steps])
        #print("next", val)
        total += val
    return total


def star2(data):
    """Solve puzzle for star 2."""
    total = 0
    for row in data:
        print("row", row)
        steps = [[0] + row]
        step = row
        while any(v != 0 for v in step):
            step = row_diff(step)
            steps.append([0] + step)
        for i in range(len(steps)-2, -1, -1):
            steps[i][0] = steps[i][1] - steps[i+1][0]
            #print(i, steps[i])
        val = steps[0][0]
        #print("prev", val)
        total += val
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