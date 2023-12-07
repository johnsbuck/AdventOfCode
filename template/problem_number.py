""" Advent of Code <YEAR> - Problem <PROBLEM_NUMBER> (https://adventofcode.com/<YEAR>/day/<PROBLEM_NUMBER>)
"""
from typing import List
import re


def get_input(filename: str = "input.txt") -> List[List[int]]:
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
            pass
    return data


def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 1 Solution
        """
    data = get_input(filename)
    pass


def part_two(filename: str = "input.txt"):
    """ Second part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 2 Solution
        """
    pass


if __name__ == "__main__":
    print("Advent of Code - <YEAR> - Problem <PROBLEM_NUMBER>")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
