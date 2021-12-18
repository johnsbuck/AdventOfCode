import re


def part_one():
    boards = []
    callouts = []
    with open("input.txt", "r") as f:
        # Get callouts
        callouts = [int(x) for x in next(f)[:-1].split(",")]

        # Ignore newline
        next(f)

        # Get each board
        boards.append([])
        for line in f:
            if line == "\n":
                boards.append([])
            else:
                boards[-1].append([int(x) for x in re.findall(r'\d+', line)])

    # Find winning bingo board
    last = None
    found = -1
    for call in callouts:
        last = call
        for i in range(len(boards)):
            if check_bingo_board(boards[i], last):
                found = i
                break
        if found >= 0:
            break

    # Get score
    win_board = boards[found]
    score = 0
    for i in range(len(win_board)):
        for k in range(len(win_board[i])):
            if win_board[i][k] >= 0:
                score += win_board[i][k]
    score *= last
    print(score)


def check_bingo_board(board, last):
    # Check rows
    for row in board:
        mark_count = 0
        for i in range(len(row)):
            if row[i] < 0:
                mark_count += 1
            elif row[i] == last:
                row[i] = -1
                mark_count += 1
        if mark_count == len(row):
            return True

    # Check columns
    for i in range(len(board[i])):
        mark_count = 0
        for k in range(len(board)):
            if board[k][i] < 0:
                mark_count += 1
        if mark_count == len(board):
            return True

    return False


def part_two():
    boards = []
    callouts = []
    with open("input.txt", "r") as f:
        # Get callouts
        callouts = [int(x) for x in next(f)[:-1].split(",")]

        # Ignore newline
        next(f)

        # Get each board
        boards.append([])
        for line in f:
            if line == "\n":
                boards.append([])
            else:
                boards[-1].append([int(x) for x in re.findall(r'\d+', line)])

    # Find last winning bingo board
    last = None
    for call in callouts:
        valid = False
        last = call

        i = 0
        while i < len(boards):
            if check_bingo_board(boards[i], last):
                if len(boards) == 1:
                    valid = True
                    break
                del boards[i]
            else:
                i += 1

        if valid:
            break

    # Get score
    win_board = boards[0]
    score = 0
    for i in range(len(win_board)):
        for k in range(len(win_board[i])):
            if win_board[i][k] >= 0:
                score += win_board[i][k]

    score *= last
    print(score)


def main():
    print("Part One")
    part_one()
    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
