from dataclasses import dataclass


def chunks(lst, n):
    """Yield successive n-sized chunks from lst - https://stackoverflow.com/a/312464"""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


@dataclass
class Point:
    x: int
    y: int

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __hash__(self):
        return 65537 * self.x + self.y
