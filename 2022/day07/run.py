#!/usr/bin/env python3

from pathlib import Path


def cd(tree, cwd_path):
    cwd = tree
    for dir in cwd_path:
        cwd = cwd[dir]
    return cwd


def parse_data(input):
    """Parse input data."""
    return input.split("\n")


def build_tree(data):
    cwd_path = ["/"]
    tree = {
        "/": {},
    }
    cwd = tree["/"]
    for line in data:
        if line.startswith("$ cd /"):
            cwd_path = ["/"]
            cwd = tree["/"]
        elif line.startswith("$ cd .."):
            cwd_path.pop()
            cwd = cd(tree, cwd_path)
        elif line.startswith("$ cd "):
            cwd_path.append(line[5:])
            cwd = cd(tree, cwd_path)
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            cwd[line[4:]] = {}
        else:
            size, f = line.split(" ")
            cwd[f] = int(size)
    return tree


def dir_size(tree):
    tree_size = 0
    for k, v in tree.items():
        if isinstance(tree[k], dict):
            tree_size += dir_size(tree[k])
        elif isinstance(tree[k], int):
            tree_size += v
        else:
            raise ValueError
    return tree_size


def filter_size(tree, result, size):
    tree_size = 0
    for k, v in tree.items():
        if isinstance(tree[k], dict):
            sub_size = filter_size(tree[k], result, size)
            if sub_size <= size:
                result.append((k, sub_size))
            tree_size += sub_size
        elif isinstance(tree[k], int):
            tree_size += v
        else:
            raise ValueError
    return tree_size


def star1(data):
    """Solve puzzle for star 1."""
    tree = build_tree(data)
    # size = dir_size(tree)

    result = []
    total_size = filter_size(tree, result, 100000)

    filtered_size = 0
    for x in result:
        _, size = x
        filtered_size += size
    return filtered_size


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
