#!/usr/bin/env python3

from pathlib import Path


def parse_data(input):
    """Parse input data."""
    result = [line for line in input.split("\n\n")]
    drawing = list(result[0].split("\n"))
    actions = list(result[1].split("\n"))
    drawing.reverse()
    return (drawing, actions)


def build_state(drawing):
    # Initialize each stack with corresponding label
    header = [int(x) for x in drawing[0].split(" ") if x != ""]
    # print(header)
    state = {}
    for i in header:
        state[i] = []
    # Fill each stack
    for line in drawing[1:]:
        for i, pos in zip(range(1, len(header) + 1), range(1, 4 * len(header), 4)):
            # print(f"{i}:{pos} = {line[pos]}")
            if line[pos] != " ":
                state[i].append(line[pos])
    return state


def operate_crane_9000(state, actions):
    for action in actions:
        # Move n from stack1 to stack2
        _, num, _, stack1, _, stack2 = action.split(" ")
        num = int(num)
        stack1 = int(stack1)
        stack2 = int(stack2)
        items = [state[stack1].pop() for _ in range(num)]
        state[stack2].extend(items)
    return state


def operate_crane_9001(state, actions):
    for action in actions:
        # Move n from stack1 to stack2
        _, num, _, stack1, _, stack2 = action.split(" ")
        num = int(num)
        stack1 = int(stack1)
        stack2 = int(stack2)
        items = [state[stack1].pop() for _ in range(num)]
        items.reverse()
        state[stack2].extend(items)
    return state


def top_crate_message(state):
    top = [state[stack].pop() for stack in state.keys()]
    message = "".join(top)
    return message


def star1(data):
    """Solve puzzle for star 1."""
    drawing, actions = data
    state = build_state(drawing)
    state = operate_crane_9000(state, actions)
    return top_crate_message(state)


def star2(data):
    """Solve puzzle for star 2."""
    drawing, actions = data
    state = build_state(drawing)
    state = operate_crane_9001(state, actions)
    return top_crate_message(state)


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
