import copy


def follow_instructions(columns, instructions, reverse):
    columns = copy.deepcopy(columns)

    for (amount, source, destination) in instructions:
        to_move = columns[source][-1 * amount :]
        if reverse:
            to_move.reverse()
        columns[source] = columns[source][: -1 * amount]
        columns[destination] += to_move

    return columns


def a(parsed_input):
    (input_columns, instructions) = parsed_input

    columns = follow_instructions(input_columns, instructions, reverse=True)

    return "".join(stack[-1] for stack in columns.values())


def b(parsed_input):
    (input_columns, instructions) = parsed_input

    columns = follow_instructions(input_columns, instructions, reverse=False)

    return "".join(stack[-1] for stack in columns.values())


def parse_input(input_path):
    reading_crates = True
    columns = {}
    instructions = []

    crate_lines = []

    with open(input_path) as f:
        for line in f:
            line = line.strip("\n")
            if line == "":
                reading_crates = False

                n_columns = (len(crate_lines[0]) + 1) // 4
                for i in range(n_columns):
                    columns[i + 1] = []

                for crates in crate_lines[-2::-1]:
                    for i, v in enumerate(crates[1::4]):
                        if v != " ":
                            columns[i + 1].append(v)
            elif reading_crates:
                crate_lines.append(line)
            else:
                split = line.split()
                instructions.append(tuple(map(int, (split[1], split[3], split[5]))))

    return (columns, instructions)


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/05/real.txt")
    print(f"Day 05 - A - {a(parsed_input)}")
    print(f"Day 05 - B - {b(parsed_input)}")
else:
    from .util import *
