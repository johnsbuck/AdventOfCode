from collections import deque
from functools import reduce


def part_one():
    data = get_input()

    output = 0
    for i in range(len(data)):
        for k in range(len(data[i])):
            if is_low_point(data, i, k):
                output += data[i][k] + 1

    print(output)


def is_low_point(data, i, k):
    neighbors = get_neighbors(data, i, k)
    for point in neighbors:
        if data[i][k] >= data[point[0]][point[1]]:
            return False
    return True


def get_neighbors(data, i, k):
    neighbors = [(i-1, k), (i+1, k), (i, k-1), (i, k+1)]

    i = 0
    while i < len(neighbors):
        if neighbors[i][0] < 0 or neighbors[i][0] >= len(data):
            del neighbors[i]
        elif neighbors[i][1] < 0 or neighbors[i][1] >= len(data[i]):
            del neighbors[i]
        else:
            i += 1

    return neighbors


def part_two():
    data = get_input()

    low_points = []
    for i in range(len(data)):
        for k in range(len(data[i])):
            if is_low_point(data, i, k):
                low_points.append((i, k))

    marked = set([])
    basins = []

    for point in low_points:
        queue = deque([point])
        curr_basin = 0
        while len(queue) > 0:
            curr = queue.popleft()
            if curr in marked:
                continue
            if data[curr[0]][curr[1]] == 9:
                continue
            marked.add(curr)
            curr_basin += 1
            queue += get_neighbors(data, curr[0], curr[1])
        if curr_basin > 0:
            basins.append(curr_basin)

    print(reduce((lambda x, y: x * y), sorted(basins)[-3:]))


def get_input(filename="input.txt"):
    data = []
    with open(filename, "r") as f:
        for row in f:
            data.append([])
            for cell in row[:-1]:
                data[-1].append(int(cell))
    return data


def main():
    print("Part One")
    part_one()
    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
