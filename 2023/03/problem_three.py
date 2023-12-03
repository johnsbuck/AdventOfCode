""" Advent of Code 2023 - Problem 3 (https://adventofcode.com/2023/day/3)
"""
from typing import Union, Type, List, Tuple


class Node:
    def __init__(self, x: Union[int, str]):
        self._val = x
        self._visited = False

    @property
    def value(self):
        return self._val

    @property
    def visited(self):
        return self._visited
    def lock_to_int(self):
        self._val = int(self._val)

    def visit(self) -> int:
        self._visited = True
        return self._val

    def append(self, x: str):
        self._val += x

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return self.__str__()


def get_input(filename: str = "input.txt",
              conv_type: Union[Type[int], Type[float], Type[str]] = int) -> 'list(conv_type)':
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
            num_node = None
            for c in row[:-1]:
                if c.isnumeric():
                    if num_node:
                        num_node.append(c)
                    else:
                        num_node = Node(c)
                    data[-1].append(num_node)
                else:
                    if num_node:
                        num_node.lock_to_int()
                        num_node = None
                    data[-1].append(c)
            if num_node:
                num_node.lock_to_int()
    return data


def find_moves_pt_one(moves: List[Tuple[int, int]], x: int, y: int, grid: List[List[Union[str, Node]]]) -> int:
    output = 0
    for move in moves:
        curr = (x + move[0], y + move[1])
        if 0 <= curr[0] < len(grid) and 0 <= curr[1] < len(grid[0]) and type(grid[curr[0]][curr[1]]) is Node:
            output += grid[curr[0]][curr[1]].value * (not grid[curr[0]][curr[1]].visited)
            grid[curr[0]][curr[1]].visit()
    return output


def find_moves_pt_two(moves: List[Tuple[int, int]], x: int, y: int, grid: List[List[Union[str, Node]]]) -> int:
    output = []
    visited = set([])
    for move in moves:
        curr = (x + move[0], y + move[1])
        if 0 <= curr[0] < len(grid) and 0 <= curr[1] < len(grid[0]) and type(grid[curr[0]][curr[1]]) is Node and\
                grid[curr[0]][curr[1]] not in visited:
            output.append(grid[curr[0]][curr[1]].value)
            visited.add(grid[curr[0]][curr[1]])
    if len(output) == 2:
        return output[0] * output[1]
    return 0

def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 1 Solution
        """
    MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    data = get_input(filename, str)

    output = 0
    for i in range(len(data)):
        for k in range(len(data[i])):
            if type(data[i][k]) is str and data[i][k] != '.':
                output += find_moves_pt_one(MOVES, i, k, data)
    return output


def part_two(filename: str = "input.txt"):
    """ Second part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 2 Solution
        """
    MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    data = get_input(filename, str)

    output = 0
    for i in range(len(data)):
        for k in range(len(data[i])):
            if type(data[i][k]) is str and data[i][k] == '*':
                output += find_moves_pt_two(MOVES, i, k, data)
    return output


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 03")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
