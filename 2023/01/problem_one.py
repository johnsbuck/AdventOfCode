""" Advent of Code 2023 - Problem 1 (https://adventofcode.com/2022/day/1)
"""
import csv
import re
from typing import Union, Type


def get_input(filename: str = "input.txt", conv_type: Union[Type[int], Type[float], Type[str]] = int) -> 'list(type)':
    """Retrieve file input from Advent of Code (expected to be csv)

        Arguments:
            filename (str): The text file to input. (Default: "input.txt")
            conv_type (type): The python type to convert the data to. (Default: int)

        Returns:
            (list(conv_type)) A list of inputs formatted to the given python type.
        """
    data = [[]]

    with open(filename, 'r') as f:
        for row in csv.reader(f):
            if len(row) == 0:
                data.append([])
            else:
                data[-1] += row
                data[-1][-1] = conv_type(data[-1][-1])

    return data[0]


def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Number of total calories.
        """
    data = get_input(filename, str)
    output = 0
    for row in data:
        digits = re.findall("[0-9]", row)
        num = int(digits[0] + digits[-1])
        output += num
    return output


def part_two(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Number of total calories.
        """
    data = get_input(filename, str)
    DIGIT_NAMES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    DIGIT_DICT = {DIGIT_NAMES[i]: str(i) for i in range(len(DIGIT_NAMES))}
    pattern = '(?=(' + '|'.join(DIGIT_NAMES) + "|[0-9]" + '))'
    output = 0
    for row in data:
        digits = re.findall(pattern, row)
        if len(digits[0]) > 1:
            digits[0] = DIGIT_DICT[digits[0]]
        if len(digits[-1]) > 1:
            digits[-1] = DIGIT_DICT[digits[-1]]
        num = int(digits[0] + digits[-1])
        output += num
    return output


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 01")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
