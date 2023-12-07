""" Advent of Code 2023 - Problem 6 (https://adventofcode.com/2023/day/6)
"""
from typing import List
import re

import numpy as np


def get_input(filename: str = "input.txt", conv_type: 'type' = int) -> 'List[List[conv_type]]':
    """Retrieve file input from Advent of Code (expected to be csv)

        Arguments:
            filename (str): The text file to input. (Default: "input.txt")
            conv_type (type): The python type to convert the data to. (Default: int)

        Returns:
            (list(conv_type)) A list of inputs formatted to the given python type.
        """
    data = []

    with open(filename, 'r') as f:
        for row in f:
            row = row.replace('\n', '')
            data.append([conv_type(x) for x  in re.split("\s+", row)[1:]])
    return data


def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 1 Solution
        """
    data = get_input(filename, conv_type=int)
    output = 1
    for i in range(len(data[0])):
        roots = np.roots([-1, data[0][i], -data[1][i] - .01])
        output *= np.floor(roots[0]) - np.ceil(roots[1]) + 1
    return int(output)


def part_two(filename: str = "input.txt"):
    """ Second part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 2 Solution
        """
    data = [int(''.join(x)) for x in get_input(filename, conv_type=str)]
    print(data)
    roots = np.roots([-1, data[0], -data[1] - .01])
    return int(np.floor(roots[0])) - int(np.ceil(roots[1])) + 1


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 06")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
