""" Advent of Code 2023 - Problem 5 (https://adventofcode.com/2023/day/5)
"""
from typing import List, Dict
import math


def get_input(filename: str = "input.txt") -> Dict[str, List[int|List[int]]]:
    """Retrieve file input from Advent of Code (expected to be csv)

        Arguments:
            filename (str): The text file to input. (Default: "input.txt")

        Returns:
            (list(conv_type)) A list of inputs formatted to the given python type.
        """
    data = {}

    with open(filename, 'r') as f:
        header = True
        last_key = None
        for row in f:
            row = row.replace('\n', '')
            if header:
                header = False
                data_input = row.split(': ')
                data[data_input[0]] = [int(x) for x in data_input[1].split(' ')]
            elif len(row) > 0 and row[0].isalpha():
                last_key = row[:-1]
                data[last_key] = []
            elif len(row) > 0:
                data[last_key].append([int(x) for x in row.split(' ')])
    return data


def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 1 Solution
        """
    data = get_input(filename)
    INPUT_KEY = "seeds"
    KEY_PATH = ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 'water-to-light map',
                'light-to-temperature map', 'temperature-to-humidity map', 'humidity-to-location map']

    output = math.inf
    for seed in data[INPUT_KEY]:
        curr_id = seed
        for key in KEY_PATH:
            for seed_map in data[key]:
                l = seed_map[1]
                r = seed_map[1] + seed_map[2]
                if l <= curr_id < r:
                    curr_id = seed_map[0] + curr_id - seed_map[1]
                    break
            if key == KEY_PATH[-1] and curr_id < output:
                output = curr_id
    return output


def part_two(filename: str = "input.txt"):
    """ Second part of problem
    NOTE: This runs into a huge time lag. Need to replace with set-range comparisons with bisecting sets on given
    scenarios. But that is too much work for a problem I know how to solve and I want to enjoy myself!

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 2 Solution
        """
    data = get_input(filename)
    INPUT_KEY = "seeds"
    KEY_PATH = ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 'water-to-light map',
                'light-to-temperature map', 'temperature-to-humidity map', 'humidity-to-location map']

    new_input = []
    for i in range(0, len(data[INPUT_KEY]), 2):
        new_input += list(range(data[INPUT_KEY][i], data[INPUT_KEY][i] + data[INPUT_KEY][i+1]))
    data[INPUT_KEY] = new_input
    print(new_input)

    output = math.inf
    for seed in data[INPUT_KEY]:
        curr_id = seed
        for key in KEY_PATH:
            for seed_map in data[key]:
                l = seed_map[1]
                r = seed_map[1] + seed_map[2]
                if l <= curr_id < r:
                    curr_id = seed_map[0] + curr_id - seed_map[1]
                    break
            if key == KEY_PATH[-1] and curr_id < output:
                output = curr_id
    return output


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 5")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
