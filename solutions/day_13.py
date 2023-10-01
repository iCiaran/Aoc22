import json
from enum import Enum
from functools import cmp_to_key


class Order(Enum):
    IN_ORDER = -1
    EQUAL = 0
    OUT_OF_ORDER = 1


def a(parsed_input):
    pairs = chunks(parsed_input, 2)
    return sum(
        i + 1 for i, pair in enumerate(pairs) if compare(*pair) == Order.IN_ORDER
    )


def b(parsed_input):
    divider_a = [[2]]
    divider_b = [[6]]
    packets = parsed_input + [divider_a] + [divider_b]

    sorted_packets = sorted(packets, key=cmp_to_key(lambda l, r: compare(l, r).value))

    index_a = sorted_packets.index(divider_a) + 1
    index_b = sorted_packets.index(divider_b) + 1

    return index_a * index_b


def parse_input(input_path):
    with open(input_path) as f:
        lines = [json.loads(line) for line in f if line != "\n"]
    return lines


def compare(left, right):
    left_is_list = type(left) == list
    right_is_list = type(right) == list

    if left_is_list and right_is_list:
        return compare_lists(left, right)
    elif left_is_list:
        return compare_lists(left, [right])
    elif right_is_list:
        return compare_lists([left], right)
    else:
        return compare_numbers(left, right)


def compare_for_cmp(left, right):
    return compare(left, right).value


def compare_lists(left, right):
    for left_item, right_item in zip(left, right):
        result = compare(left_item, right_item)
        if result != Order.EQUAL:
            return result

    if len(left) == len(right):
        return Order.EQUAL
    elif len(left) > len(right):
        return Order.OUT_OF_ORDER
    else:
        return Order.IN_ORDER


def compare_numbers(left, right):
    if left == right:
        return Order.EQUAL
    elif left > right:
        return Order.OUT_OF_ORDER
    else:
        return Order.IN_ORDER


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/13/real.txt")
    print(f"Day 13 - A - {a(parsed_input)}")
    print(f"Day 13 - B - {b(parsed_input)}")
else:
    from .util import *
