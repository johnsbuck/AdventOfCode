""" Advent of Code 2023 - Problem 4 (https://adventofcode.com/2023/day/4)
"""
from typing import List
import re


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
        for row in f:
            data.append([])
            numbers = row.split(': ')[1]
            winning_nums, picked_nums = numbers.split(' | ')
            winning_nums = [int(x) for x in re.sub("^ (\d)", "\g<1>", winning_nums).replace("  ", ' ').split(' ')]
            picked_nums = [int(x) for x in re.sub(r" (\d)([ |\n])", r"\g<1>\g<2>", picked_nums)\
                .replace('\n', '').split(' ')]
            data[-1].append(winning_nums)
            data[-1].append(picked_nums)
    return data


def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 1 Solution
        """
    data = get_input(filename)

    output = 0
    for card in data:
        winning, picked = card
        count = 0
        for num in picked:
            count += num in winning
        if count:
            output += 2 ** (count - 1)
    return output


def part_two(filename: str = "input.txt"):
    """ Second part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 2 Solution
        """
    data = get_input(filename)
    card_wins = [1 for _ in range(len(data))]
    for i in range(len(data)):
        card = data[i]
        winning, picked = card
        count = 0
        for num in picked:
            count += num in winning
        card_wins[i] += count

    total_cards = [1 for _ in range(len(data))]
    for i in range(len(card_wins)):
        count = card_wins[i] - 1
        for k in range(i+1, min(i + card_wins[i], len(card_wins))):
            if count > 0:
                count -= 1
            total_cards[k] += 1 * total_cards[i]
    return sum(total_cards)


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 04")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
