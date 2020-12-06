import math


def get_input(filename="input.txt.txt"):
    board_passes = []
    with open(filename, "r+") as file:
        for line in file:
            board_passes.append(line.rstrip())
    return board_passes


def get_ids(board_passes: "list[str]") -> "list[int]":
    ids = []
    for board in board_passes:
        low, high = 0, 127
        for c in board[:7]:
            if c == "B":
                low = math.ceil((low + high) / 2)
            else:
                high = math.floor((low + high) / 2)
        row = low
        low, high = 0, 7
        for c in board[7:]:
            if c == "R":
                low = math.ceil((low + high) / 2)
            else:
                high = math.floor((low + high) / 2)
        col = low
        ids.append(8 * row + col)
    return ids


def get_solution_5a(board_passes: "list[str]") -> int:
    return max(get_ids(board_passes))


def get_solution_5b(board_passes: "list[str]") -> int:
    ids = get_ids(board_passes)
    ids = sorted(ids)
    possibles = []
    for i in range(1, len(ids)):
        if ids[i] - ids[i-1] == 2:
            possibles.append(ids[i] - 1)
    return possibles


passes = get_input()
print(get_solution_5a(passes))
print(get_solution_5b(passes))
