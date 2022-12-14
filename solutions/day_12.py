from collections import deque


def a(parsed_input):
    grid, start, end = parsed_input

    dirs = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]
    height = len(grid)
    width = len(grid[0])

    to_visit = deque([(start, 0)])
    visited = set()

    while len(to_visit) > 0:
        next, dist = to_visit.popleft()

        if next in visited:
            continue

        if next == end:
            return dist

        visited.add(next)

        for dir in dirs:
            temp = next + dir
            if temp.x >= 0 and temp.y >= 0 and temp.x < width and temp.y < height and (grid[temp.y][temp.x] - grid[next.y][next.x]) <= 1:
                to_visit.append((temp, dist + 1))

    return -1


def b(parsed_input):
    grid, _, end = parsed_input

    dirs = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]
    height = len(grid)
    width = len(grid[0])

    to_visit = deque([(end, 0)])
    visited = set()

    while len(to_visit) > 0:
        next, dist = to_visit.popleft()

        if next in visited:
            continue

        if grid[next.y][next.x] == 0:
            return dist

        visited.add(next)

        for dir in dirs:
            temp = next + dir
            if temp.x >= 0 and temp.y >= 0 and temp.x < width and temp.y < height and (grid[temp.y][temp.x] - grid[next.y][next.x]) >= -1:
                to_visit.append((temp, dist + 1))

    return -1


def parse_input(input_path):
    with open(input_path) as f:
        lines = [list(map(lambda h: ord(h) - ord("a"), line.strip())) for line in f]

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == ord("S") - ord("a"):
                start = Point(x, y)
                lines[y][x] = 0
            elif lines[y][x] == ord("E") - ord("a"):
                end = Point(x, y)
                lines[y][x] = ord("z") - ord("a")

    return (lines, start, end)


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/12/real.txt")
    print(f"Day 12 - A - {a(parsed_input)}")
    print(f"Day 12 - B - {b(parsed_input)}")
else:
    from .util import *
