def find_sizes(tree, current, sizes):
    if current in sizes:
        return sizes[current], sizes

    files_total = sum(file_size for (_, file_size) in tree[current]["files"])
    dirs_total = sum(find_sizes(tree, dir, sizes)[0] for dir in tree[current]["dirs"])
    total = dirs_total + files_total

    sizes[current] = total
    return total, sizes


def a(tree):
    _, sizes = find_sizes(tree, "/", {})

    max_total_size = 100000

    return sum(size for size in sizes.values() if size <= max_total_size)


def b(tree):
    total_size, sizes = find_sizes(tree, "/", {})

    sorted_sizes = sorted(sizes.values())
    total_space = 70000000
    needed_space = 30000000

    return next(filter(lambda size: total_space - (total_size - size) >= needed_space, sorted_sizes), -1)


def parse_input(input_path):
    tree = {"/": {"files": [], "dirs": []}}
    cwd = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            split = line.split()
            if split[0] == "$":
                if split[1] == "cd":
                    if split[2] == "..":
                        cwd.pop()
                    else:
                        cwd.append(split[2])
            else:
                cwd_string = "-".join(cwd)
                if split[0] == "dir":
                    next_cwd = f"{cwd_string}-{split[1]}"
                    tree[next_cwd] = {"files": [], "dirs": []}
                    tree[cwd_string]["dirs"].append(next_cwd)
                else:
                    tree[cwd_string]["files"].append((split[1], int(split[0])))

    return tree


if __name__ == "__main__":
    from util import *

    parsed_input = parse_input("inputs/07/real.txt")
    print(f"Day 07 - A - {a(parsed_input)}")
    print(f"Day 07 - B - {b(parsed_input)}")
else:
    from .util import *
