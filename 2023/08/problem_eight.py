""" Advent of Code 2023 - Problem 8 (https://adventofcode.com/2023/day/8)
"""
from typing import List
import re
from math import lcm


def get_input(filename: str = "input.txt") -> List[List[int]]:
    """Retrieve file input from Advent of Code (expected to be csv)

        Arguments:
            filename (str): The text file to input. (Default: "input.txt")
            conv_type (type): The python type to convert the data to. (Default: int)

        Returns:
            (list(conv_type)) A list of inputs formatted to the given python type.
        """
    data = ["",{}]

    with open(filename, 'r') as f:
        row_count = 0
        for row in f:
            if row_count == 0:
                row_count += 1
                data[0] = row[:-1]
            elif row_count == 1:
                row_count += 1
            else:
                row = row.replace('\n', '').replace('(', '').replace(')', '')
                result = re.split(r" \= ", row)
                data[1][result[0]] = re.split(", ", result[1])

    return data


def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 1 Solution
        """
    data = get_input(filename)
    path, node_dict = data
    PATH_IDX = {'L': 0, 'R': 1}

    get_path = lambda: PATH_IDX[path[output % len(path)]]
    output = 0
    step = get_path()

    # Go through pathing until we reach end (ZZZ)
    node = 'AAA'
    while node != 'ZZZ':
        node = node_dict[node][step]

        output += 1
        step = get_path()
    return output


def part_two(filename: str = "input.txt"):
    """ Second part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 2 Solution
        """
    data = get_input(filename)
    path, node_dict = data
    PATH_IDX = {'L': 0, 'R': 1}

    get_path = lambda: PATH_IDX[path[output % len(path)]]
    output = 0
    step = get_path()

    # Find cycles for each node
    nodes = [k for k in node_dict if k.endswith("A")]
    steps_to_end = [0] * len(nodes)
    while not all(steps_to_end):
        for i in range(len(nodes)):
            nodes[i] = node_dict[nodes[i]][step]
            if nodes[i].endswith("Z"):
                if not steps_to_end[i]:
                    steps_to_end[i] = output + 1
        output += 1
        step = get_path()

    # Return point where each cycle ends (Least Common Multiple)
    return lcm(*steps_to_end)


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 8")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
