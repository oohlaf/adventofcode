#!/usr/bin/env python3

from copy import deepcopy
from pathlib import Path


def parse_data(input):
    """Parse input data."""
    monkeys = []
    for line in input.split("\n"):
        line = line.strip()
        if line:
            if line[0] == "M":
                monkeys.append(
                    {
                        "inspect": 0,
                    }
                )
            elif line[0] == "S":
                monkeys[-1]["items"] = [int(i) for i in line[16:].split(",")]
            elif line[0] == "O":
                monkeys[-1]["op"] = line[21]
                if line[23:] == "old":
                    monkeys[-1]["op_old"] = line[23:]
                else:
                    monkeys[-1]["op_val"] = int(line[23:])
            elif line[0] == "T":
                monkeys[-1]["test"] = int(line[19:])
            elif line[0] == "I":
                if line[3] == "t":
                    monkeys[-1]["true"] = int(line[25:])
                elif line[3] == "f":
                    monkeys[-1]["false"] = int(line[26:])
    return monkeys


def play_round(monkeys):
    for m in monkeys:
        while m["items"]:
            i = m["items"].pop(0)
            m["inspect"] += 1
            value = m.get("op_val", i)
            if m["op"] == "*":
                i *= value
            else:
                i += value
            i //= 3
            if i % m["test"]:
                monkeys[m["false"]]["items"].append(i)
            else:
                monkeys[m["true"]]["items"].append(i)


def print_status(round, monkeys):
    print(f"After round {round}, the monkeys are holding items with these worry levels:")
    for index, m in enumerate(monkeys):
        print(f"Monkey {index}: {m['items']}")


def print_inspects(round, monkeys):
    print(f"== After round {round} ==")
    for index, m in enumerate(monkeys):
        print(f"Monkey {index} inspected items {m['inspect']} times.")


def monkey_business(monkeys):
    inspects = []
    for m in monkeys:
        inspects.append(m["inspect"])
    inspects.sort(reverse=True)
    return inspects[0] * inspects[1]


def star1(data):
    """Solve puzzle for star 1."""
    for r in range(20):
        play_round(data)
        print_status(r + 1, data)
    print_inspects(r + 1, data)
    return monkey_business(data)


def play_round_worried(monkeys, red):
    for m in monkeys:
        while m["items"]:
            i = m["items"].pop(0)
            m["inspect"] += 1
            value = m.get("op_val", i)
            if m["op"] == "*":
                i *= value
            else:
                i += value
            i %= red
            if i % m["test"]:
                monkeys[m["false"]]["items"].append(i)
            else:
                monkeys[m["true"]]["items"].append(i)


def star2(data):
    """Solve puzzle for star 2."""
    red = 1
    for m in data:
        red *= m["test"]
    for r in range(10000):
        play_round_worried(data, red)
        if r in [0, 19, 999, 8999, 9999]:
            # print_status(r + 1, data)
            print_inspects(r + 1, data)
    return monkey_business(data)


def solve(input):
    data = parse_data(input)
    data2 = deepcopy(data)
    yield star1(data)
    yield star2(data2)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())
