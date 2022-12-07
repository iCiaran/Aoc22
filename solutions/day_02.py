def a(rounds):
    score = 0

    selection_points = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    outcome_points = {
        "X": {"A": 3, "B": 0, "C": 6},
        "Y": {"A": 6, "B": 3, "C": 0},
        "Z": {"A": 0, "B": 6, "C": 3},
    }

    for [opponent, me] in rounds:
        score += outcome_points[me][opponent] + selection_points[me]

    return score


def b(rounds):
    score = 0

    outcome_points = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    selection_points = {
        "Z": {"A": 2, "B": 3, "C": 1},
        "Y": {"A": 1, "B": 2, "C": 3},
        "X": {"A": 3, "B": 1, "C": 2},
    }

    for [opponent, goal] in rounds:
        score += outcome_points[goal] + selection_points[goal][opponent]

    return score


def parse_input(input_path):
    with open(input_path) as f:
        lines = [line.split() for line in f]
    return lines


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/02/real.txt")
    print(f"Day 02 - A - {a(parsed_input)}")
    print(f"Day 02 - B - {b(parsed_input)}")
else:
    from .util import *
