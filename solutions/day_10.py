def get_x_values(instructions):
    x = 1
    x_values = []
    for instruction in instructions:
        x_values.append(x)
        if instruction != "noop":
            _, v = instruction.split()
            x_values.append(x)
            x += int(v)

    return x_values


def a(instructions):
    x_values = get_x_values(instructions)
    sample_cycles = [20, 60, 100, 140, 180, 220]
    sum_of_strengths = 0

    for cycle in sample_cycles:
        sum_of_strengths += cycle * x_values[cycle - 1]

    return sum_of_strengths


def b(instructions):
    x_values = get_x_values(instructions)
    line = ""
    for i, x in enumerate(x_values):

        if x - 1 <= (i % 40) <= x + 1:
            line += "#"
        else:
            line += "."

        if (i + 1) % 40 == 0:
            # Uncomment print to see output:
            # print(line)

            # ####..##..###...##....##.####...##.####.
            # ...#.#..#.#..#.#..#....#.#.......#....#.
            # ..#..#....###..#..#....#.###.....#...#..
            # .#...#....#..#.####....#.#.......#..#...
            # #....#..#.#..#.#..#.#..#.#....#..#.#....
            # ####..##..###..#..#..##..#.....##..####.

            line = ""

    return "ZCBAJFJZ"


def parse_input(input_path):
    with open(input_path) as f:
        instructions = [line.strip() for line in f]
    return instructions


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/10/real.txt")
    print(f"Day 10 - A - {a(parsed_input)}")
    print(f"Day 10 - B - {b(parsed_input)}")
else:
    from .util import *
