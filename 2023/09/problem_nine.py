""" Advent of Code 2023 - Problem 9 (https://adventofcode.com/2023/day/9)
"""
from typing import List
import csv
from functools import reduce


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
        for row in csv.reader(f, delimiter=' '):
            data.append([int(x) for x in row])
    return data


def find_next_element(series: List[int]) -> int:
    differences = [series[i] - series[i-1] for i in range(1, len(series))]
    last_elements = [series[-1], differences[-1]]

    # Find each iteration for each delta of series until constant
    while differences.count(differences[0]) != len(differences):
        differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]
        last_elements.append(differences[-1])

    # Get next element from each delta
    output = last_elements[-1]
    for i in range(len(last_elements) - 2, -1, -1):
        output = last_elements[i] + output
    return output


def find_prev_element(series: List[int]) -> int:
    differences = [series[i] - series[i-1] for i in range(1, len(series))]
    first_elements = [series[0], differences[0]]

    # Find each iteration for each delta of series until constant
    while differences.count(differences[0]) != len(differences):
        differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]
        first_elements.append(differences[0])

    # Get next element from each delta
    output = first_elements[-1]
    for i in range(len(first_elements) - 2, -1, -1):
        output = first_elements[i] - output
    return output


def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 1 Solution
        """
    data = get_input(filename)

    output = 0
    for row in data:
        output += find_next_element(row)
    return output


def part_two(filename: str = "input.txt"):
    """ Second part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 2 Solution
        """
    data = get_input(filename)

    output = 0
    for row in data:
        output += find_prev_element(row)
    return output


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 9")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
