from collections import deque


class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = set(children)

    def __str__(self):
        output = self.val + "->\""

        for child in self.children:
            output += child + ','

        if output[-1] == ',':
            return output[:-1] + "\""

        return output + "\""

    def __repr__(self):
        return self.__str__()


def part_one():
    data = get_input()

    print(data)

    total_paths = 0
    queue = deque([(data["start"], set())])

    while len(queue) > 0:
        curr, marked = queue.popleft()

        # print(curr, marked)

        if curr in marked:
            continue

        if curr.val == "end":
            total_paths += 1
        else:
            new_marked = None
            if curr.val.islower():
                new_marked = marked.union(set([curr]))
            else:
                new_marked = marked.copy()
            for child in curr.children:
                queue.append((data[child], new_marked))

    print(total_paths)


def part_two():
    data = get_input()

    print(data)

    total_paths = 0
    queue = deque([(data["start"], set(), False)])

    while len(queue) > 0:
        curr, marked, small_cave_revisit = queue.popleft()

        # print(curr, marked)

        if curr in marked:
            if curr.val == "start" or small_cave_revisit:
                continue
            else:
                small_cave_revisit = True

        if curr.val == "end":
            total_paths += 1
        else:
            new_marked = None
            if curr.val.islower():
                new_marked = marked.union({curr})
            else:
                new_marked = marked.copy()
            for child in curr.children:
                queue.append((data[child], new_marked, small_cave_revisit))

    print(total_paths)


def get_input(filename="input.txt"):
    nodes = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split('-')
            node_one = Node(line[0], [])
            node_two = Node(line[1], [])
            if node_one.val in nodes:
                nodes[node_one.val].children.add(node_two.val)
            else:
                node_one.children.add(node_two.val)
                nodes[node_one.val] = node_one

            if node_two.val in nodes:
                nodes[node_two.val].children.add(node_one.val)
            else:
                node_two.children.add(node_one.val)
                nodes[node_two.val] = node_two

    return nodes


def main():
    print("Part One")
    part_one()
    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
