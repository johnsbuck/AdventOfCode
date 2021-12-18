import re


def part_one():
    lines = get_input("input.txt")

    i = 0
    while i < len(lines):
        # Remove all diagonals
        if lines[i][0][0] != lines[i][1][0] and lines[i][0][1] != lines[i][1][1]:
            del lines[i]
        else:
            # Swap for all lines to go left-to-right or up-to-down
            if lines[i][0][0] > lines[i][1][0] or (lines[i][0][0] == lines[i][1][0] and lines[i][0][1] > lines[i][1][1]):
                lines[i][0], lines[i][1] = lines[i][1], lines[i][0]
            i += 1

    output = 0
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    # For each line
    for line in lines:
        x = list(range(line[0][0], line[1][0] + 1))
        y = list(range(line[0][1], line[1][1] + 1))
        points = []
        if len(x) == 1:
            points = [(x[0], y[i]) for i in range(len(y))]
        else:
            points = [(x[i], y[0]) for i in range(len(x))]

        for point in points:
            matrix[point[0]][point[1]] += 1

    # Get number of times a point is greater than or equal to 2
    for i in range(len(matrix)):
        for k in range(len(matrix)):
            if matrix[i][k] >= 2:
                output += 1

    print(output)


def part_two():
    lines = get_input("input.txt")

    for line in lines:
        # Swap for all lines to go left-to-right or up-to-down
        if line[0][0] > line[1][0] or (line[0][0] == line[1][0] and line[0][1] > line[1][1]):
            line[0], line[1] = line[1], line[0]

    output = 0
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        x = list(range(line[0][0], line[1][0] + 1))
        y = list(range(line[0][1], line[1][1] + 1))
        if len(y) == 0:
            y = list(range(line[0][1], line[1][1] - 1, -1))
        points = []
        if len(x) == 1:
            points = [(x[0], y[i]) for i in range(len(y))]
        elif len(y) == 1:
            points = [(x[i], y[0]) for i in range(len(x))]
        else:
            points = [(x[i], y[i]) for i in range(len(x))]

        for point in points:
            matrix[point[0]][point[1]] += 1

    # Get number of times point is greater than or equal to 2
    for i in range(len(matrix)):
        for k in range(len(matrix)):
            if matrix[i][k] >= 2:
                output += 1

    print(output)


def get_input(filename="input.txt"):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            x1, y1, x2, y2 = re.findall(r"(\d+),(\d+) -> (\d+),(\d+)\n", line)[0]
            lines.append([(int(x1), int(y1)), (int(x2), int(y2))])
    return lines


def main():
    print("Part One")
    part_one()
    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
