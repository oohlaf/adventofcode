#!/usr/bin/env python3

from pathlib import Path
import re


def parse_data(input):
    """Parse input data."""
    schematic = [[ch for ch in line] for line in input.splitlines()]
    return schematic


def is_symbol(x, y, data):
    c = data[y][x]
    non_symbols = ".0123456789"
    if c in non_symbols:
        return False
    return True


def parse_part_numbers(input, w, h):
    # make coordinate grid with empty lists
    parts = []
    for _ in range(h):
        row = []
        for _ in range(w):
            row.append([])
        parts.append(row)
    y = 0
    for line in input.splitlines():
        for m in re.finditer(r"\d+", line):
            # find all digits
            val = int(m[0])
            y1 = y - 1
            if y1 < 0:
                y1 = 0
            y2 = y + 2
            if y2 > h:
                y2 = y + 1
            for j in range(y1, y2):
                x1 = m.span()[0] - 1
                if x1 < 0:
                    x1 = 0
                x2 = m.span()[1] + 1
                if x2 > w:
                    x2 = m.span()[1]
                # fill coordinate grid with values surrounding a digit string
                for i in range(x1, x2):
                    if j == y and i in range(m.span()[0], m.span()[1]):
                        # skip positions of the part number itself
                        continue
                    #print("i", i, "j", j, "val", val)
                    parts[j][i].append(val)
        y += 1
    return parts


def star1(data, parts):
    """Solve puzzle for star 1."""
    w = len(data[0])
    h = len(data)
    total = 0
    for j in range(w):
        for i in range(h):
            if is_symbol(i, j, data):
                val = sum(parts[j][i])
                #print("i", i, "j", j, "sym", data[j][i], "val", val)
                total += val
    return total


def star2(data, parts):
    """Solve puzzle for star 2."""
    w = len(data[0])
    h = len(data)
    total = 0
    for j in range(w):
        for i in range(h):
            if data[j][i] == '*' and len(parts[j][i]) == 2:
                gear = 1
                for g in parts[j][i]:
                    gear *= g
                #print("i", i, "j", j, "sym", data[j][i], "gear", gear)
                total += gear
    return total


def solve(input):
    data = parse_data(input)
    w = len(data[0])
    h = len(data)
    parts = parse_part_numbers(input, w, h)
    yield star1(data, parts)
    yield star2(data, parts)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())