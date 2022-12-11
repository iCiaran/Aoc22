def find_visible(line, horizontal, n):
    highest = -1
    visible = []
    for index, height in line:
        if height > highest:
            highest = height
            visible.append(Point(index, n) if horizontal else Point(n, index))

    return visible


def a(grid):
    height = len(grid)
    width = len(grid[0])
    visible = set()

    for y in range(height):
        line = list(enumerate(grid[y]))

        visible.update(find_visible(line, True, y))
        visible.update(find_visible(line[::-1], True, y))

    for x in range(width):
        line = list(enumerate(row[x] for row in grid))

        visible.update(find_visible(line, False, x))
        visible.update(find_visible(line[::-1], False, x))

    return len(visible)


def b(grid):
    height = len(grid)
    width = len(grid[0])
    best_view = 0

    dirs = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            current_view = 1

            for dir in dirs:
                distance = 1

                while True:
                    next = Point(x + dir.x * distance, y + dir.y * distance)

                    if next.x == 0 or next.x == width - 1 or next.y == 0 or next.y == height - 1:
                        break

                    if grid[next.y][next.x] >= grid[y][x]:
                        break

                    distance += 1

                current_view *= distance

            if current_view > best_view:
                best_view = current_view

    return best_view


def parse_input(input_path):
    with open(input_path) as f:
        grid = [list(map(int, line.strip())) for line in f]
    return grid


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/08/real.txt")
    print(f"Day 08 - A - {a(parsed_input)}")
    print(f"Day 08 - B - {b(parsed_input)}")
else:
    from .util import *
