#!/usr/bin/env python3

from pathlib import Path


def parse_data(input):
    """Parse input data."""
    result = [(line[0], int(line[2:])) for line in input.split("\n")]
    return result


MOVES = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def head_movement(pos, step):
    x, y = pos
    dx, dy = step
    return (x + dx, y + dy)


def tail_movement(head, tail):
    x, y = head
    a, b = tail
    dx = abs(x - a)
    dy = abs(y - b)
    if dx < 2 and dy < 2:
        return (a, b)
    if dx == 2:
        a += (x - a) // dx
        if dy == 1:
            b += y - b
    if dy == 2:
        b += (y - b) // dy
        if dx == 1:
            a += x - a
    return (a, b)


def print_title(header):
    print(f"== {header} ==\n\n")


def print_grid(head, tail, width, height):
    grid = [["." for _ in range(width)] for _ in range(height)]
    x, y = tail
    grid[height - 1][0] = "s"
    grid[height - 1 - y][x] = "T"
    x, y = head
    grid[height - 1 - y][x] = "H"
    for line in grid:
        for c in line:
            print(c, end="")
        print("\n", end="")
    print("\n")
    return grid


def star1(data):
    """Solve puzzle for star 1."""
    width = 6
    height = 5
    head = (0, 0)
    tail = (0, 0)
    head_path = [head]
    tail_path = [tail]
    print_title("Initial State")
    print_grid(head, tail, width, height)
    for (move, n) in data:
        print_title(f"{move} {n}")
        step = MOVES[move]
        for _ in range(n):
            head = head_movement(head, step)
            head_path.append(head)
            tail = tail_movement(head, tail)
            tail_path.append(tail)
            print_grid(head, tail, width, height)
    return len((set(tail_path)))


def star2(data):
    """Solve puzzle for star 2."""


def solve(input):
    data = parse_data(input)
    yield star1(data)
    yield star2(data)


def main():
    input_file = Path(__file__).parent / "test_input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())
