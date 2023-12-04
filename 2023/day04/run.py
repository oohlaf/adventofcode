#!/usr/bin/env python3

from pathlib import Path
import re


def parse_data(input):
    """Parse input data."""
    cards = {}
    for line in input.splitlines():
        card_line = line.split(":")
        card_id = int(card_line[0].replace("Card ", ""))
        card_data = card_line[1].split("|")
        winning_numbers = []
        my_numbers = []
        for number in re.findall(r"\d+", card_data[0]):
            number = int(number.strip())
            winning_numbers.append(number)
        for number in re.findall(r"\d+", card_data[1]):
            number = int(number.strip())
            my_numbers.append(number)
        cards[card_id] = (winning_numbers, my_numbers)
    return cards


def card_matches(w, m):
    matches = 0
    for n in w:
        if n in m:
            matches += 1
    return matches


def star1(data):
    """Solve puzzle for star 1."""
    total_score = 0
    for id, (w, m) in data.items():
        score = 0
        matches = card_matches(w, m)
        if matches:
            score = 2 ** (matches - 1)
        #print ("id", id, "score", score)
        total_score += score
    return total_score


def star2(data):
    """Solve puzzle for star 2."""
    inventory = {}
    # init inventory with originals
    for id in data:
        inventory[id] = 1
    for id, (w, m) in data.items():
        matches = card_matches(w, m)
        #print ("id", id, "matches", matches)
        # do for as many items as we have in the inventory
        for _ in range(inventory[id]):
            for m in range(id+1, id+1+matches):
                inventory[m] += 1
    return sum(inventory.values())    


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