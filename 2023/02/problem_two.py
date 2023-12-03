""" Advent of Code 2023 - Problem 2 (https://adventofcode.com/2023/day/2)
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
    data = []
    COLORS = ['green', 'red', 'blue']

    with open(filename, 'r') as f:
        for row in f:
            data.append({})
            row = re.split(r', |; |: |\n', row)
            for i in range(1, len(row) - 1):
                key_color = None
                for color in COLORS:
                    if color in row[i]:
                        key_color = color
                        break
                num = re.match('[0-9]+', row[i]).group(0)

                if key_color not in data[-1]:
                    data[-1][key_color] = int(num)
                else:
                    data[-1][key_color] = max(int(num), data[-1][key_color])

    return data


def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Number of total calories.
        """
    data = get_input(filename, str)
    COLORS_DICT = {'red': 12, 'green': 13, 'blue': 14}

    output = 0
    for i in range(len(data)):
        valid = True
        for color in COLORS_DICT:
            if data[i][color] > COLORS_DICT[color]:
                valid = False
                break
        if valid:
            output += i + 1
    return output


def part_two(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Number of total calories.
        """
    data = get_input(filename, str)

    output = 0
    for i in range(len(data)):
        power = 1
        for k in data[i]:
            power *= data[i][k]
        output += power

    return output


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 01")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
