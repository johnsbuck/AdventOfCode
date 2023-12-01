""" Advent of Code 2022 - Problem 6 (https://adventofcode.com/2022/day/7)
"""
from collections import deque


class Node:

    def __init__(self, parent: 'Node' = None, size: int = 0):
        self.parent = parent
        self.children = {}
        self.size = size

    def __str__(self, level=0, name="/"):
        ret = "\t" * level + name + ": " + repr(self.size) + " " + str(len(self.children)) + "\n"
        for child in self.children:
            ret += self.children[child].__str__(level + 1, child)
        return ret

    def __repr__(self):
        return '<tree node representation>'


def get_input(filename="input.txt") -> 'deque[str]':
    """Retrieve file input from Advent of Code (expected to be csv)

    Arguments:
        filename (str): The text file to input. (Default: "input.txt")

    Returns:
        (list(str)) A list of inputs.
    """
    data = deque([])
    with open(filename, 'r') as f:
        for line in f:
            data.append(line[:-1].split(' '))
    return data


def cd(directory: str, root: Node, curr: Node):
    if directory == '..':
        return curr.parent
    if directory == '/':
        return root
    return curr.children[directory]


def ls(commands: str, curr: Node):
    while commands and commands[0][0] != "$":
        child = commands.popleft()
        size = 0
        if child[0] != "dir":
            size = int(child[0])
        if child[1] not in curr.children:
            curr.children[child[1]] = Node(curr, size)


def size_traversal(root: Node):
    for key in root.children:
        root.size += size_traversal(root.children[key])

    return root.size


def sum_traversal(root: Node, max_size: int) -> int:
    output = 0

    if len(root.children) == 0:
        return 0

    if root.size <= max_size:
        output += root.size

    for key in root.children:
        output += sum_traversal(root.children[key], max_size)

    return output


def del_traversal(root: Node, deleted_space: int) -> int:
    output = 0

    if len(root.children) == 0:
        return 0

    if root.size >= deleted_space:
        output = root.size

    for key in root.children:
        new_val = del_traversal(root.children[key], deleted_space)
        if output == 0:
            output = new_val
        elif new_val != 0 and output > new_val:
            output = new_val

    return output


def part_one(filename="input.txt") -> int:
    """ First part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (int) Part one answer.
    """
    commands = get_input(filename)
    root = Node()
    curr = root

    while commands:
        comm = commands.popleft()
        if comm[0] != "$":
            raise ValueError("Improper sequencing")
        if comm[1] == "cd":
            curr = cd(comm[2], root, curr)
        elif comm[1] == "ls":
            ls(commands, curr)

    size_traversal(root)

    return sum_traversal(root, 100000)


def part_two(filename="input.txt", max_space: int = 70000000, needed_space: int = 30000000) -> int:
    """ Second part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")
        max_space (int): The maximum filesystem disk space. (Default: 70000000)
        needed_space (int): The amount of disk space needed. (Default: 30000000)

    Returns:
        (int) Part two answer.
    """
    commands = get_input(filename)
    root = Node()
    curr = root

    while commands:
        comm = commands.popleft()
        if comm[0] != "$":
            raise ValueError("Improper sequencing")
        if comm[1] == "cd":
            curr = cd(comm[2], root, curr)
        elif comm[1] == "ls":
            ls(commands, curr)

    size_traversal(root)
    space_removed = needed_space - (max_space - root.size)

    return del_traversal(root, space_removed)


if __name__ == "__main__":
    print("Advent of Code - 2022 - Problem 07")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
