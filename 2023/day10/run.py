#!/usr/bin/env python3

from pathlib import Path
import numpy as np


def parse_data(input):
    """Parse input data."""
    grid = []
    i = -1
    j = -1
    for line in input.splitlines():
        row = [c for c in line]
        grid.append(row)
        if i < 0:
            j += 1
            i = line.find('S')
    return (j, i), grid


NORTH = "|7F"
EAST = "-7J"
SOUTH = "|LJ"
WEST = "-LF"


def star1(data):
    """Solve puzzle for star 1."""
    (y, x) = data[0]
    grid = data[1]
    w = len(grid[0])
    h = len(grid)
    distance = np.zeros((h, w), dtype=int)
    # skip when revisiting the starting position
    distance[y][x] = -1
    todo = [(y, x, 0)]
    while len(todo):
        (y, x, i) = todo.pop(0)
        if (y > 0) and (grid[y-1][x] in NORTH) and (distance[y-1][x] == 0):
            distance[y-1][x] = i + 1
            todo.append((y-1,x,i+1))
        if (x < w-1) and (grid[y][x+1] in EAST) and (distance[y][x+1] == 0):
            distance[y][x+1] = i + 1
            todo.append((y,x+1,i+1))
        if (y < h-1) and (grid[y+1][x] in SOUTH) and (distance[y+1][x] == 0):
            distance[y+1][x] = i + 1
            todo.append((y+1,x,i+1))
        if (x > 0) and (grid[y][x-1] in WEST) and (distance[y][x-1] == 0):
            distance[y][x-1] = i + 1
            todo.append((y,x-1,i+1))
    #print(distance)
    return(distance.max())


NEXT_PIPE = {
    'S': [(-1,0,NORTH), (0,1,EAST), (1,0,SOUTH), (0,-1,WEST)],
    '|': [(-1,0,NORTH), (1,0,SOUTH)],
    '-': [(0,-1,WEST), (0,1,EAST)],
    'L': [(-1,0,NORTH), (0,1,EAST)],
    'J': [(-1,0,NORTH), (0,-1,WEST)],
    '7': [(1,0,SOUTH), (0,-1,WEST)],
    'F': [(1,0,SOUTH), (0,1,EAST)],
    '.': []
}

START = {
    (-2, 0): '|',
    (-1, 1): 'F',
    (-1, -1): '7',
    (0, -2): '-',
    (0, 2): '-',
    (1, 1): 'L',
    (1, -1): 'J',
    (2, 0): '|'
}

def next_paths(path, grid):
    (y, x) = path[-1]
    w = len(grid[0])
    h = len(grid)
    todo = []
    for (dy, dx, peek) in NEXT_PIPE[grid[y][x]]:
        (b, a) = (y+dy, x+dx)
        if 0 <= b < h and 0 <= a < w and ((len(path)<=2 and grid[b][a] in peek) or
                                          (len(path)>2 and (grid[b][a]=='S' or (b,a) not in path[1:]))):
            new_path = path.copy()
            new_path.append((b, a))
            todo.append(new_path)
    return todo


def star2(data):
    """Solve puzzle for star 2."""
    (y, x) = data[0]
    grid = data[1]
    w = len(grid[0])
    h = len(grid)
    paths = [[(y, x)]]
    found = False
    while not found:
        path = paths.pop(0)
        todo = next_paths(path, grid)
        for peek in todo:
            (y, x) = peek[-1]
            if grid[y][x] == 'S':
                found = True
                paths = [peek]
                break
            elif grid[y][x] != '.':
                paths.append(peek)
    if not found:
        return
    path = paths[0]
    print(path)
    # Create grid with just the found cycle
    cycle = np.zeros((h, w), dtype='|S1')
    for (y,x) in path:
        cycle[y][x] = grid[y][x]
    (y, x) = path[1]
    (b, a) = path[-2]
    (dy, dx) = (y-b, x-a)
    (y, x) = path[0]
    cycle[y][x] = START[(dy,dx)]
    for y in range(h):
        crossed = 0
        for x in range(w):
            if cycle[y][x] == b'|':
                crossed += 1
            elif cycle[y][x] in [b'-']:
                continue
            elif cycle[y][x] in [b'L']:
                prev = 'L'
            elif cycle[y][x] in [b'F']:
                prev = 'F'
            elif cycle[y][x] in [b'7']:
                if prev == 'L':
                    crossed += 1
                    prev = ''
            elif cycle[y][x] in [b'J']:
                if prev == 'F':
                    crossed += 1
                    prev = ''
            elif crossed % 2:
                cycle[y][x] = 'I'
            else:
                cycle[y][x] = '0'
    print(cycle)
    return (cycle==b'I').sum()


def solve(input):
    data = parse_data(input)
    yield star1(data)
    yield star2(data)


def main():
    np.set_printoptions(threshold=np.inf,linewidth=800)
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())