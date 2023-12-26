#!/usr/bin/env python3

from pathlib import Path
from itertools import pairwise
import numpy as np


def parse_data(input):
    """Parse input data."""
    report = []
    for line in input.splitlines():
        data = line.split()
        conditions = data[0]
        damage_groups = [int(n) for n in data[1].split(',')]
        report.append((conditions, damage_groups))
    return report


def create_dfa(groups):
    # [1,1,3] = ".#.#.###."
    dfa = "."
    for damage in groups:
        for _ in range(damage):
            dfa += "#"
        dfa += "."
    return dfa


def create_stt(dfa):
    # create state transition table as numpy matric
    # columns are the state/position in dfa counting from 1
    # row 0 is .
    # row 1 is #
    w = len(dfa) + 1
    # 0 is no transition
    stt = np.zeros((2,w), dtype=int)
    i = 1
    for (cur, nxt) in pairwise(dfa):
        if cur == '.' and nxt == '#':
            stt[0][i] = i
            stt[1][i] = i + 1
        elif cur == '#':
            if nxt == '.':
                stt[0][i] = i + 1
            elif nxt == '#':
                stt[1][i] = i + 1
        i += 1
    # self loop for . at end
    stt[0][w-1] = w - 1
    return stt


# transform stt row to a adjacency matrix for that input
def adj_matrix(stt_row):
    adj = np.zeros((stt_row.shape[0], stt_row.shape[0]), dtype=int)
    for i, v in np.ndenumerate(stt_row):
        if v:
            adj[i[0]][v] = 1
    return adj


def process(input, adj_oper, adj_dmgd):
    w = len(input) + 1
    # rows = input chars (first char is 1)
    # columns = states
    # value is counter of how many times state has been visited
    counter = np.zeros((w,adj_oper.shape[0]), dtype=int)
    # start state is 1, on input 0
    counter[0][1] = 1
    for i, c in enumerate(input):
        for j, v in enumerate(counter[i]):
            if c in ".?":
                counter[i+1] += v * adj_oper[j]
            if c in "#?":
                counter[i+1] += v * adj_dmgd[j]
    # last two states are the end states of the dfa, sum is number of possibilities
    return counter[-1][-2] + counter[-1][-1]


def star1(data):
    """Solve puzzle for star 1."""
    total = 0
    for (cond, dm) in data:
        dfa = create_dfa(dm)
        #print(dfa)
        stt = create_stt(dfa)
        #print(stt)
        adj_oper = adj_matrix(stt[0])
        adj_dmgd = adj_matrix(stt[1])
        #print(adj_oper)
        #print(adj_dmgd)
        total += process(cond, adj_oper, adj_dmgd)
    return total


def star2(data):
    """Solve puzzle for star 2."""
    total = 0
    for (cond, dm) in data:
        cond = '?'.join([cond] * 5)
        dm = dm * 5
        dfa = create_dfa(dm)
        #print(dfa)
        stt = create_stt(dfa)
        #print(stt)
        adj_oper = adj_matrix(stt[0])
        adj_dmgd = adj_matrix(stt[1])
        #print(adj_oper)
        #print(adj_dmgd)
        total += process(cond, adj_oper, adj_dmgd)
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