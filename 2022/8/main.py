""" Advent of Code 2022 - Problem 8 (https://adventofcode.com/2022/day/8)
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
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append([int(c) for c in line if c != '\n'])
    return data


def part_one(filename="input.txt") -> int:
    """ First part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (int) Part one answer.
    """
    data = get_input(filename)
    tree_set = set()

    # Left Visible
    for i in range(len(data)):
        highest = -1
        for k in range(len(data[i])):
            if highest < data[i][k]:
                tree_set.add((i, k))
                highest = data[i][k]

    # Right Visible
    for i in range(len(data) - 1, -1, -1):
        highest = -1
        for k in range(len(data[i]) - 1, -1, -1):
            if highest < data[i][k]:
                tree_set.add((i, k))
                highest = data[i][k]

    # Top Visible
    for i in range(len(data)):
        highest = -1
        for k in range(len(data[i])):
            if highest < data[k][i]:
                tree_set.add((k, i))
                highest = data[k][i]

    # Bottom Visible
    for i in range(len(data) - 1, -1, -1):
        highest = -1
        for k in range(len(data[i]) - 1, -1, -1):
            if highest < data[k][i]:
                tree_set.add((k, i))
                highest = data[k][i]

    return len(tree_set)


def part_two(filename="input.txt") -> int:
    """ Second part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (int) Part two answer.
    """
    data = get_input(filename)
    scenic_scores = [[1 for k in range(len(data[i]))] for i in range(len(data))]

    for i in range(1, len(data) - 1):
        for k in range(1, len(data) - 1):
            # Left
            count = 0
            for a in range(k - 1, -1, -1):
                count += 1
                if data[i][a] >= data[i][k]:
                    break
            scenic_scores[i][k] *= count

            # Right
            count = 0
            for a in range(k+1, len(data)):
                count += 1
                if data[i][a] >= data[i][k]:
                    break
            scenic_scores[i][k] *= count

            # Top
            count = 0
            for a in range(i - 1, -1, -1):
                count += 1
                if data[a][k] >= data[i][k]:
                    break
            scenic_scores[i][k] *= count

            # Bottom
            count = 0
            for a in range(i + 1, len(data)):
                count += 1
                if data[a][k] >= data[i][k]:
                    break
            scenic_scores[i][k] *= count

    return max(map(max, scenic_scores))


if __name__ == "__main__":
    print("Advent of Code - 2022 - Problem 08")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
