#!/usr/bin/env python3

from pathlib import Path

import numpy as np

def parse_data(input):
    """Parse input data."""
    games = {}
    for line in input.splitlines():
        game_line = line.split(":")
        game_id = int(game_line[0].replace("Game ", ""))
        game_list = []
        for hand_line in game_line[1].split(";"):
            red = 0
            green = 0
            blue = 0
            for color_line in hand_line.split(","):
                color_line = color_line.strip()
                color = color_line.split(" ")
                if color[1] == "red":
                    red = int(color[0])
                elif color[1] == "green":
                    green = int(color[0])
                elif color[1] == "blue":
                    blue = int(color[0])
            game_list.append((red, green, blue))
        games[game_id] = np.array(game_list)
    return games
        

def star1(data):
    """Solve puzzle for star 1."""
    T = np.array((12, 13, 14))
    total = 0
    for id, game in data.items():
        M = game.max(axis=0)
        C = np.less_equal(M, T)
        #print("Game", id, "Max", M, "Result", C)
        if np.all(C):
            total += id
    return total


def star2(data):
    """Solve puzzle for star 2."""
    total = 0
    for id, game in data.items():
        M = game.max(axis=0)
        P = np.prod(M)
        #print("Game", id, "Max", M, "Result", P)
        total += P
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