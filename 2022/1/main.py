""" Advent of Code 2022 - Problem 1 (https://adventofcode.com/2022/day/1)
"""
import csv


def get_input(filename="input.txt", conv_type=int) -> 'list(type)':
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

    return data


def part_one(filename="input.txt") -> int:
    """ First part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (int) Number of total calories.
    """
    data = get_input(filename, int)
    output = -1
    for row in data:
        total_cal = sum(row)
        if total_cal > output:
            output = total_cal
    return output


def part_two(filename="input.txt", top_elf_count=3) -> int:
    """ Second part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")
        top_elf_count (int): Number of top calories elves to add. (Default: 3)

    Returns:
        (int) Number of total calories.
    """
    data = get_input(filename)

    output = [-1 for _ in range(top_elf_count)]

    for row in data:
        total_cal = sum(row)
        output.append(total_cal)
        output = sorted(output, reverse=True)[:3]

    return sum(output)


if __name__ == "__main__":
    print("Advent of Code - 2022 - Problem 01")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
