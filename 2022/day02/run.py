#!/usr/bin/env python3

import numpy as np

from pathlib import Path


MOVE_DICT = {
    # Opponent moves
    "A": np.array([1, 0, 0]),  # Rock
    "B": np.array([0, 1, 0]),  # Paper
    "C": np.array([0, 0, 1]),  # Scissors

    # My moves
    "X": np.array([1, 0, 0]),  # Rock
    "Y": np.array([0, 1, 0]),  # Paper
    "Z": np.array([0, 0, 1]),  # Scissors
}

# Opp x Me
# 0 = loss, 3 = tie, 6 = win
OUTCOME_SCORES = np.array([[3, 6, 0], [0, 3, 6], [6, 0, 3]])

# X = 1, Y = 2, Z = 3
SHAPE_SCORES = np.array([1, 2, 3])


def parse_data(input):
    """Parse input data."""
    game_play = [(line[0], line[2]) for line in input.split("\n")]
    return game_play


def game(move):
    opp, me = move
    opp_move = MOVE_DICT[opp]
    my_move = MOVE_DICT[me]
    game_move = np.outer(opp_move, my_move)
    outcome_score = np.multiply(game_move, OUTCOME_SCORES)
    shape_score = np.multiply(my_move, SHAPE_SCORES)
    score = np.sum(outcome_score) + np.sum(shape_score)
    return score


def star1(data):
    """Solve puzzle for star 1."""
    score = 0
    for round in data:
        score += game(round)
    return score


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
