from queue import PriorityQueue


def part_one():
    data = get_input()

    final_score = None
    END_GOAL = [len(data) - 1, len(data[0]) - 1]

    queue = PriorityQueue()
    queue.put((dist(0, 0, END_GOAL[0], END_GOAL[1]), 0, 0, 0))
    marked = set()

    while not queue.empty():
        heuristic, score, x, y = queue.get()
        if (x, y) in marked:
            continue
        if x == END_GOAL[0] and y == END_GOAL[1]:
            final_score = score
            break
        marked.add((x, y))
        for neigh in get_neighbors(x, y, END_GOAL):
            if neigh not in marked:
                new_score = score + data[neigh[0]][neigh[1]]
                queue.put((dist(neigh[0], neigh[1], END_GOAL[0], END_GOAL[1]) + new_score, new_score, neigh[0], neigh[1]))

    print(final_score)


def part_two():
    data = get_input()

    final_score = None
    END_GOAL = [len(data) * 5 - 1, len(data[0]) * 5 - 1]

    queue = PriorityQueue()
    queue.put((dist(0, 0, END_GOAL[0], END_GOAL[1]), 0, 0, 0))
    marked = set()

    while not queue.empty():
        heuristic, score, x, y = queue.get()
        if (x, y) in marked:
            continue
        if x == END_GOAL[0] and y == END_GOAL[1]:
            final_score = score
            break
        marked.add((x, y))
        for neigh in get_neighbors(x, y, END_GOAL):
            if neigh not in marked:
                add_score = (data[neigh[0] % len(data)][neigh[1] % len(data)] +
                             neigh[0] // len(data) + neigh[1] // len(data)) % 9
                add_score += (add_score == 0) * 9
                new_score = score + add_score
                queue.put(
                    (dist(neigh[0], neigh[1], END_GOAL[0], END_GOAL[1]) + new_score, new_score, neigh[0], neigh[1]))

    print(final_score)


def get_neighbors(x, y, goal):
    neighbors = []
    for i in [-1, 1]:
        if 0 <= x + i <= goal[0]:
            neighbors.append((x + i, y))
        if 0 <= y + i <= goal[1]:
            neighbors.append((x, y + i))
    return neighbors


def dist(x, y, a, b):
    return abs(a - x) + abs(b - y)


def get_input(filename="input.txt"):
    data = []

    with open(filename, 'r') as f:
        for line in f:
            data.append([int(x) for x in line[:-1]])

    return data


def main():
    print("Part One")
    part_one()

    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
