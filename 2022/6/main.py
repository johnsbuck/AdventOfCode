""" Advent of Code 2022 - Problem 6 (https://adventofcode.com/2022/day/6)
"""
import csv
import re
from collections import deque


def get_input(filename="input.txt") -> 'list(str)':
    """Retrieve file input from Advent of Code (expected to be csv)

    Arguments:
        filename (str): The text file to input. (Default: "input.txt")

    Returns:
        (list(str)) A list of inputs.
    """
    data = None
    with open(filename, 'r') as f:
        data = [c for c in f.readline()]
    return data


def part_one(filename="input.txt") -> str:
    """ First part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (str) Part one answer.
    """
    data = get_input(filename)
    start_stream = deque([])

    for i in range(len(data)):
        if len(start_stream) == 4:
            return i
        if data[i] not in start_stream:
            start_stream.append(data[i])
        else:
            while len(start_stream) > 0 and start_stream.popleft() != data[i]:
                continue
            start_stream.append(data[i])
    return -1


def part_two(filename="input.txt") -> str:
    """ Second part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (str) Part two answer.
    """
    data = get_input(filename)
    start_stream = deque([])

    for i in range(len(data)):
        if len(start_stream) == 14:
            return i
        if data[i] not in start_stream:
            start_stream.append(data[i])
        else:
            while len(start_stream) > 0 and start_stream.popleft() != data[i]:
                continue
            start_stream.append(data[i])
    return -1


if __name__ == "__main__":
    print("Advent of Code - 2022 - Problem 06")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
