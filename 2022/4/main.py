""" Advent of Code 2022 - Problem 3-1 (https://adventofcode.com/2022/day/4)
"""
import csv
from collections import Counter


def get_input(filename="input.txt") -> 'list(str)':
    """Retrieve file input from Advent of Code (expected to be csv)

    Arguments:
        filename (str): The text file to input. (Default: "input.txt")

    Returns:
        (list(str)) A list of inputs.
    """
    data = []

    with open(filename, 'r') as f:
        for row in csv.reader(f, delimiter=','):
            point = []
            for elf in row:
                point.append([int(x) for x in elf.split('-')])
            data.append(point)
    return data


def part_one(filename="input.txt") -> int:
    """ First part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (int) Part one answer.
    """
    data = get_input(filename)
    output = 0

    for pair in data:
        x, y = pair[0], pair[1]
        if x[0] > y[0] or x[0] == y[0] and x[1] < y[1]:
            x, y = y, x
        if x[0] <= y[0] and y[1] <= x[1]:
            output += 1
    return output


def part_two(filename="input.txt") -> int:
    """ Second part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (int) Part two answer.
    """
    data = get_input(filename)
    output = 0

    for pair in data:
        x, y = pair[0], pair[1]
        if x[0] > y[0] or x[0] == y[0] and x[1] < y[1]:
            x, y = y, x
        if x[0] <= y[0] <= x[1] or x[0] <= y[1] <= x[1]:
            output += 1
    return output


if __name__ == "__main__":
    print("Advent of Code - 2022 - Problem 04")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
