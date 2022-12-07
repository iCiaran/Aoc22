def a(elves):
    return max(map(sum, elves))


def b(elves):
    amount_per_elf = map(sum, elves)
    return sum(sorted(amount_per_elf)[-3:])


def parse_input(input_path):
    with open(input_path) as f:
        elves = f.read().split("\n\n")
    elves = [list(map(int, elf.split("\n"))) for elf in elves]
    return elves


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/01/real.txt")
    print(f"Day 01 - A - {a(parsed_input)}")
    print(f"Day 01 - B - {b(parsed_input)}")
else:
    from .util import *
