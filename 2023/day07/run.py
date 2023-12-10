#!/usr/bin/env python3

from pathlib import Path
from collections import Counter


def parse_data(input):
    """Parse input data."""
    hands = []
    for line in input.splitlines():
        data = line.split()
        hands.append((data[0], int(data[1])))
    return hands


HAND_TYPES = {
    (5, 0, 0, 0, 0): 0,
    (4, 1, 0, 0, 0): 1,
    (3, 2, 0, 0, 0): 2,
    (3, 1, 1, 0, 0): 3,
    (2, 2, 1, 0, 0): 4,
    (2, 1, 1, 1, 0): 5,
    (1, 1, 1, 1, 1): 6
}


HAND_NAMES = {
    0: "Five of a kind",
    1: "Four of a kind",
    2: "Full house",
    3: "Three of a kind",
    4: "Two pair",
    5: "One pair",
    6: "High card"
}


CARD_RANK = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'J': 3,
    'T': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12,
}


# Joker is lowest rank
CARD_RANK2 = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'J': 13,
    'T': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12
}


def type_of_hand(hand):
    freq_sorted = [0, 0, 0, 0, 0]
    freq = Counter(hand)
    for i, c in enumerate(sorted(freq.values(), reverse=True)):
        freq_sorted[i] = c
    return HAND_TYPES[tuple(freq_sorted)]


def star1(data):
    """Solve puzzle for star 1."""
    ranked = sorted(data, reverse=True, key=lambda x: (type_of_hand(x[0]), CARD_RANK[x[0][0]], CARD_RANK[x[0][1]], CARD_RANK[x[0][2]], CARD_RANK[x[0][3]], CARD_RANK[x[0][4]]))
    total = 0
    for i, (hand, bid) in enumerate(ranked):
        print(hand, bid, HAND_NAMES[type_of_hand(hand)])
        total += (i+1)*bid
    return total
    

def type_of_hand2(hand):
    freq_sorted = [0, 0, 0, 0, 0]
    freq = Counter(hand)
    jokers = 0
    if 'J' in freq:
        jokers = freq['J']
        freq.pop('J')
    for i, c in enumerate(sorted(freq.values(), reverse=True)):
        freq_sorted[i] = c
    # Add jokers to highest rank
    freq_sorted[0] += jokers
    return HAND_TYPES[tuple(freq_sorted)]


def star2(data):
    """Solve puzzle for star 2."""
    ranked = sorted(data, reverse=True, key=lambda x: (type_of_hand2(x[0]), CARD_RANK2[x[0][0]], CARD_RANK2[x[0][1]], CARD_RANK2[x[0][2]], CARD_RANK2[x[0][3]], CARD_RANK2[x[0][4]]))
    total = 0
    for i, (hand, bid) in enumerate(ranked):
        print(hand, bid, HAND_NAMES[type_of_hand(hand)])
        total += (i+1)*bid
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