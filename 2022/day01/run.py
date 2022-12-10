#!/usr/bin/env python3

from pathlib import Path


def parse_data(input):
    """Parse input data.
    
    Returns a nested list of calories per item in each elf's inventory.
    """
    inventory = [[int(calory) for calory in elf.split("\n")] for elf in input.split("\n\n")]
    return inventory


def star1(data):
    """Solve puzzle for star 1."""
    elve_totals = [sum(elf_calories) for elf_calories in data]
    maximum = max(elve_totals)
    return maximum


def star2(data):
    """Solve puzzle for star 2."""
    elf_totals = [sum(elf_calories) for elf_calories in data]
    elf_totals.sort(reverse=True)
    top_three_total = sum(elf_totals[:3])
    return top_three_total


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