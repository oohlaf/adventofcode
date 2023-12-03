#!/usr/bin/env python3
import string

from pathlib import Path

def parse_data(input, star2=False):
    """Parse input data."""
    numbers = {'one': '1 e', 'two': '2 o', 'three': '3   e', 'four': '4  r', 'five': '5  e', 'six': '6 x', 'seven': '7   n', 'eight': '8   t', 'nine': '9  e'}
    inventory = []
    for line in input.split("\n"):
        if star2:
            for i in range(len(line)):
                for k,v in numbers.items():
                    if line[i:].startswith(k):
                        line = line[:i] + line[i:].replace(k,v)
                        break
        line=line.replace(" ","")
        line=line.strip(string.ascii_lowercase)
        if len(line):
            number = int(line[0])*10 + int(line[-1])
            inventory.append(number)
    return inventory


def star1(data):
    """Solve puzzle for star 1."""
    total = sum(data)
    return total


def star2(data):
    """Solve puzzle for star 2."""
    total = sum(data)
    return total


def solve(input):
    data = parse_data(input)
    yield star1(data)
    data = parse_data(input, True)
    yield star2(data)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())