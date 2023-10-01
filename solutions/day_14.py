


def a(parsed_input):
    cave = build_cave(parsed_input)
    lowest = max(map(lambda p: p.y, cave))
    sand_spawn = Point(500, 0)

    sand_placed = 0
    while place_sand_with_void(cave, lowest, sand_spawn):
        sand_placed += 1

    return sand_placed


def b(parsed_input):
    cave = build_cave(parsed_input)
    lowest = max(map(lambda p: p.y, cave))
    sand_spawn = Point(500, 0)

    sand_placed = 0
    while sand_spawn not in cave:
        place_sand_with_floor(cave, lowest, sand_spawn)
        sand_placed += 1

    return sand_placed


def parse_input(input_path):
    paths = []
    with open(input_path) as f:
        for line in f:
            points = [
                Point(*map(int, point.split(","))) for point in line.split(" -> ")
            ]
            paths.append(points)
    return paths


def get_direction(start, finish):
    diff = finish - start

    assert bool(diff.x) ^ bool(diff.y)

    if diff.x > 0:
        return Point(1, 0)
    elif diff.x < 0:
        return Point(-1, 0)
    elif diff.y > 0:
        return Point(0, 1)
    else:
        return Point(0, -1)


def build_cave(paths):
    cave = set()

    for path in paths:
        for start, finish in zip(path, path[1:]):
            dir = get_direction(start, finish)
            current = start
            while current != finish:
                cave.add(current)
                current += dir
            cave.add(finish)

    return cave


def place_sand_with_void(cave, lowest, sand_spawn):
    down = Point(0, 1)
    down_left = Point(-1, 1)
    down_right = Point(1, 1)
    sand = sand_spawn

    while True:
        if sand.y > lowest:
            return False
        elif sand + down not in cave:
            sand += down
        elif sand + down_left not in cave:
            sand += down_left
        elif sand + down_right not in cave:
            sand += down_right
        else:
            cave.add(sand)
            return True


def place_sand_with_floor(cave, lowest, sand_spawn):
    down = Point(0, 1)
    down_left = Point(-1, 1)
    down_right = Point(1, 1)

    floor = lowest + 2
    sand = sand_spawn

    while True:
        if sand.y == floor - 1:
            cave.add(sand)
            return True
        elif sand + down not in cave:
            sand += down
        elif sand + down_left not in cave:
            sand += down_left
        elif sand + down_right not in cave:
            sand += down_right
        else:
            cave.add(sand)
            return True


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/14/real.txt")
    print(f"Day 14 - A - {a(parsed_input)}")
    print(f"Day 14 - B - {b(parsed_input)}")
else:
    from .util import *
