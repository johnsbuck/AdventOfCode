""" Advent of Code 2022 - Problem 2 (https://adventofcode.com/2022/day/2)
"""
import csv


def get_input(filename="input.txt") -> 'list(str)':
    """Retrieve file input from Advent of Code (expected to be csv)

    Arguments:
        filename (str): The text file to input. (Default: "input.txt")

    Returns:
        (list(str)) A list of inputs.
    """
    data = []

    with open(filename, 'r') as f:
        for row in csv.reader(f, delimiter=' '):
            data.append(row)
    return data


def outcome_part_one(x: str, y: str) -> int:
    DRAW_RPS_MAP = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    }

    WIN_RPS_MAP = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    pick_points = ord(y) - ord('X') + 1

    if DRAW_RPS_MAP[x] == y:
        return 3 + pick_points
    if WIN_RPS_MAP[x] == y:
        return 0 + pick_points
    return 6 + pick_points


def part_one(filename="input.txt") -> int:
    """ First part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (int) Part one answer.
    """

    data = get_input(filename)
    output = 0
    for row in data:
        output += outcome_part_one(row[0], row[1])
    return output


def outcome_part_two(x: str, y: str) -> int:
    if y == 'X':
        RPS_MAP = {'A': 'Z', 'B': 'X', 'C': 'Y'}
        output = 0
    elif y == 'Y':
        RPS_MAP = {'A': 'X', 'B': 'Y', 'C': 'Z'}
        output = 3
    else:
        RPS_MAP = {'A': 'Y', 'B': 'Z', 'C': 'X'}
        output = 6

    output += ord(RPS_MAP[x]) - ord('X') + 1
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
    for row in data:
        output += outcome_part_two(row[0], row[1])

    return output


if __name__ == "__main__":
    print("Advent of Code - 2022 - Problem 02")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
