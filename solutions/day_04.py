def a(pairs):
    count = 0

    for (a, b) in pairs:
        if (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1]):
            count += 1

    return count


def b(pairs):
    count = 0

    for (a, b) in pairs:
        if max(a[1], b[1]) - min(a[0], b[0]) <= (a[1] - a[0] + b[1] - b[0]):
            count += 1

    return count


def parse_input(input_path):
    pairs = []
    with open(input_path) as f:
        for line in f:
            split = line.strip().split(",")
            pairs.append(
                (
                    tuple(map(int, split[0].split("-"))),
                    tuple(map(int, split[1].split("-"))),
                )
            )
    return pairs


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/04/real.txt")
    print(f"Day 04 - A - {a(parsed_input)}")
    print(f"Day 04 - B - {b(parsed_input)}")
else:
    from .util import *
