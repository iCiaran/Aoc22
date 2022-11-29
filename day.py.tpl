def a(parsed_input):
    return "##DAY## A - Not Implemented"


def b(parsed_input):
    return "##DAY## B - Not Implemented"


def parse_input(input_path):
    with open(input_path) as f:
        lines = [int(line.strip()) for line in f]
    return lines


if __name__ == "__main__":
    from util import *
    parsed_input = parse_input("inputs/##DAY##/real.txt")
    print(a(parsed_input))
    print(b(parsed_input))
else:
    from .util import *
