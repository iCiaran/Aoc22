from math import lcm
import copy


def play(monkeys, rounds, lower_worry):
    monkeys = copy.deepcopy(monkeys)
    n = lcm(*map(lambda m: m["test"], monkeys))

    for _ in range(rounds):
        for monkey in monkeys:
            monkey["inspections"] += len(monkey["items"])
            while len(monkey["items"]) > 0:
                ldict = {"old": monkey["items"].pop(0)}
                exec(monkey["operation"], globals(), ldict)

                if lower_worry:
                    new = ldict["new"] // 3
                else:
                    new = ldict["new"] % n

                if new % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(new)
                else:
                    monkeys[monkey["false"]]["items"].append(new)

    return monkeys


def a(monkeys):
    sorted_monkeys = sorted(play(monkeys, 20, True), key=lambda m: m["inspections"], reverse=True)

    return sorted_monkeys[0]["inspections"] * sorted_monkeys[1]["inspections"]


def b(monkeys):
    sorted_monkeys = sorted(play(monkeys, 10000, False), key=lambda m: m["inspections"], reverse=True)

    return sorted_monkeys[0]["inspections"] * sorted_monkeys[1]["inspections"]


def parse_input(input_path):
    monkeys = []
    with open(input_path) as f:

        for i, line in enumerate(f):
            line = line.strip()
            match i % 7:
                case 0:
                    monkey = {"inspections": 0}
                case 1:
                    monkey["items"] = list(map(int, line.split(": ")[1].split(",")))
                case 2:
                    monkey["operation"] = line.split(": ")[1]
                case 3:
                    monkey["test"] = int(line.split("divisible by ")[1])
                case 4:
                    monkey["true"] = int(line.split("monkey ")[1])
                case 5:
                    monkey["false"] = int(line.split("monkey ")[1])
                case 6:
                    monkeys.append(monkey)
        monkeys.append(monkey)

    return monkeys


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/11/real.txt")
    print(f"Day 11 - A - {a(parsed_input)}")
    print(f"Day 11 - B - {b(parsed_input)}")
else:
    from .util import *
