""" Advent of Code 2022 - Problem 5 (https://adventofcode.com/2022/day/5)
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
    NUM_STACKS = 9
    start_state = [deque([]) for _ in range(NUM_STACKS)]
    moves = []

    with open(filename, 'r') as f:
        stack_inputs = True
        for row in csv.reader(f):
            if len(row) == 0:
                stack_inputs = False
                start_state = [list(x) for x in start_state]
            elif stack_inputs:
                row[0] += ' '
                vals = re.findall(r'\[([A-Z])\]\s|(?:\s{4})', row[0])
                for i in range(len(vals)):
                    if len(vals[i]) != 0:
                        start_state[i].appendleft(vals[i])
            else:
                moves.append(tuple(int(x) for x in re.findall(r'\d+', row[0])))
    return start_state, moves


def part_one(filename="input.txt") -> str:
    """ First part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (str) Part one answer.
    """
    state, moves = get_input(filename)

    for mov in moves:
        # I know there a much faster way of doing this, but moving stacks seems more fun!
        # Probably state[end-1] += state[start-1][idx_start:idx_end:-1], but meh.
        amt, start, end = mov
        for _ in range(amt):
            state[end-1].append(state[start-1].pop())

    return ''.join(x[-1] for x in state)


def part_two(filename="input.txt") -> str:
    """ Second part of problem

    Arguments:
        filename (str): The text file with problem input. (Default: "input.txt")

    Returns:
        (str) Part two answer.
    """
    state, moves = get_input(filename)

    for mov in moves:
        amt, start, end = mov
        state[end-1] += state[start-1][len(state[start-1])-amt:]
        state[start-1] = state[start-1][:len(state[start-1])-amt]

    return ''.join(x[-1] for x in state)


if __name__ == "__main__":
    print("Advent of Code - 2022 - Problem 05")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
