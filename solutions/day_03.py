def a(rucksacks):
    total_priority = 0

    for rucksack in rucksacks:
        first, second = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
        intersection = set(first).intersection(set(second))
        total_priority += get_priority(intersection.pop())

    return total_priority


def b(rucksacks):
    total_priority = 0

    for group in chunks(rucksacks, 3):
        intersection = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        total_priority += get_priority(intersection.pop())

    return total_priority


def get_priority(item):
    val = ord(item)
    return val - 96 if val > 96 else val - 38


def parse_input(input_path):
    with open(input_path) as f:
        rucksacks = [line.strip() for line in f]
    return rucksacks


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/03/real.txt")
    print(f"Day 03 - A - {a(parsed_input)}")
    print(f"Day 03 - B - {b(parsed_input)}")
else:
    from .util import *
