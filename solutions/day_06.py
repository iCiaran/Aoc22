def find_marker(buffer, marker_length):
    for i in range(len(buffer) - marker_length + 1):
        most_recent = buffer[i : i + marker_length]
        if len(most_recent) == len(set(most_recent)):
            return i + marker_length
    return -1


def a(buffer):
    return find_marker(buffer, 4)


def b(buffer):
    return find_marker(buffer, 14)


def parse_input(input_path):
    with open(input_path) as f:
        return f.readline().strip()


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/06/real.txt")
    print(f"Day 06 - A - {a(parsed_input)}")
    print(f"Day 06 - B - {b(parsed_input)}")
else:
    from .util import *
