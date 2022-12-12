def move_tail(head, tail):
    dist = tail.manhattan_distance(head)

    if dist == 2:
        if tail.x == head.x and tail.y < head.y:
            tail += Point(0, 1)
        elif tail.x == head.x and tail.y > head.y:
            tail += Point(0, -1)
        elif tail.y == head.y and tail.x < head.x:
            tail += Point(1, 0)
        elif tail.y == head.y and tail.x > head.x:
            tail += Point(-1, 0)
    elif dist > 2:
        x_diff = head.x - tail.x
        y_diff = head.y - tail.y

        if x_diff > 0 and y_diff > 0:
            tail += Point(1, 1)
        elif x_diff > 0 and y_diff < 0:
            tail += Point(1, -1)
        elif x_diff < 0 and y_diff > 0:
            tail += Point(-1, 1)
        elif x_diff < 0 and y_diff < 0:
            tail += Point(-1, -1)

    return tail


def a(parsed_input):
    dirs = {"L": Point(-1, 0), "R": Point(1, 0), "D": Point(0, -1), "U": Point(0, 1)}
    head = Point(0, 0)
    tail = Point(0, 0)

    tail_visited = set([Point(0, 0)])

    for dir, distance in parsed_input:
        for _ in range(distance):
            head += dirs[dir]
            tail = move_tail(head, tail)
            tail_visited.add(tail)

    return len(tail_visited)


def b(parsed_input):
    dirs = {"L": Point(-1, 0), "R": Point(1, 0), "D": Point(0, -1), "U": Point(0, 1)}
    knots = [Point(0, 0) for _ in range(10)]

    tail_visited = set([Point(0, 0)])

    for dir, distance in parsed_input:
        for _ in range(distance):
            knots[0] += dirs[dir]
            for i in range(1, 10):
                knots[i] = move_tail(knots[i - 1], knots[i])
            tail_visited.add(knots[9])

    return len(tail_visited)


def parse_input(input_path):
    lines = []
    with open(input_path) as f:
        for line in f:
            direction, distance = line.strip().split()
            lines.append((direction, int(distance)))
    return lines


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/09/real.txt")
    print(f"Day 09 - A - {a(parsed_input)}")
    print(f"Day 09 - B - {b(parsed_input)}")
else:
    from .util import *
