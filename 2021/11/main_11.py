from collections import deque


def part_one():
    data = get_input()

    TOTAL_STEPS = 100

    total_flashes = 0

    for n in range(TOTAL_STEPS):
        # print("Step:", n + 0)
        # for line in data:
        #     print(line)
        # print()

        flash_point = []
        for i in range(len(data)):
            for k in range(len(data)):
                data[i][k] += 1
                if data[i][k] > 9:
                    flash_point.append((i, k))
        queue = deque(flash_point)
        while len(queue) > 0:
            curr = queue.popleft()
            if data[curr[0]][curr[1]] == 0:
                continue
            else:
                data[curr[0]][curr[1]] = 0
                total_flashes += 1
                neighbors = get_flash_neighbors(curr, data)
                for neigh in neighbors:
                    data[neigh[0]][neigh[1]] += 1
                    if data[neigh[0]][neigh[1]] > 9:
                        queue.append(neigh)

    # print("Step:", TOTAL_STEPS)
    # for line in data:
    #     print(line)
    # print()

    print(total_flashes)


def part_two():
    data = get_input()

    TOTAL_STEPS = 100

    final_step = 0
    while True:
        for line in data:
            print(line)
        print()

        flash_point = []
        for i in range(len(data)):
            for k in range(len(data)):
                data[i][k] += 1
                if data[i][k] > 9:
                    flash_point.append((i, k))
        queue = deque(flash_point)

        flashes = 0
        while len(queue) > 0:
            curr = queue.popleft()
            if data[curr[0]][curr[1]] == 0:
                continue
            else:
                flashes += 1
                data[curr[0]][curr[1]] = 0
                neighbors = get_flash_neighbors(curr, data)
                for neigh in neighbors:
                    data[neigh[0]][neigh[1]] += 1
                    if data[neigh[0]][neigh[1]] > 9:
                        queue.append(neigh)

        final_step += 1
        if flashes == len(data) * len(data[i]):
            break

    print(final_step)


def get_input(filename="input.txt"):
    data = []

    with open(filename, 'r') as f:
        for line in f:
            data.append([])
            for c in line:
                if c == '\n':
                    continue
                data[-1].append(int(c))

    return data


def get_flash_neighbors(point, data):
    neighbors = []
    for i in range(-1, 2):
        for k in range(-1, 2):
            if i == k == 0:
                continue
            new_point = (point[0] + i, point[1] + k)
            if new_point[0] < 0 or new_point[0] >= len(data):
                continue
            if new_point[1] < 0 or new_point[1] >= len(data[i]):
                continue
            if data[new_point[0]][new_point[1]] == 0:
                continue
            neighbors.append(new_point)
    return neighbors


def main():
    print("Part One")
    part_one()
    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
