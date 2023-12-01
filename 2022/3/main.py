""" Advent of Code 2022 - Problem 3 (https://adventofcode.com/2022/day/3)
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
        for row in csv.reader(f):
            data.append([c for c in row[0]])
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
    for row in data:
        dup_item = list(set(row[:len(row)//2]).intersection(set(row[len(row)//2:])))[0]
        dup_item = ord(dup_item.lower()) - ord('a') + 1 + (26 * dup_item.isupper())
        output += dup_item
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

    elf_group = []

    for row in data:
        elf_group.append(set(row))
        if len(elf_group) == 3:
            dup_item = list(set.intersection(*elf_group))[0]
            dup_item = ord(dup_item.lower()) - ord('a') + 1 + (26 * dup_item.isupper())
            output += dup_item
            elf_group = []

    return output


if __name__ == "__main__":
    print("Advent of Code - 2022 - Problem 03")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
