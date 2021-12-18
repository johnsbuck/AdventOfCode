from operator import itemgetter


def part_one():
    data, folds = get_input()

    for fold in folds:

        fold_set = set()

        for point in data:
            if fold[0] == 'x':
                if point[0] > fold[1]:
                    point = (fold[1] - (point[0] - fold[1]), point[1])
                fold_set.add(point)
            else:
                if point[1] > fold[1]:
                    point = (point[0], fold[1] - (point[1] - fold[1]))
                fold_set.add(point)

        data = fold_set

        # Only doing first fold
        break
    print(len(data))


def part_two():
    data, folds = get_input()

    for fold in folds:

        fold_set = set()

        for point in data:
            if fold[0] == 'x':
                if point[0] > fold[1]:
                    point = (fold[1] - (point[0] - fold[1]), point[1])
                fold_set.add(point)
            else:
                if point[1] > fold[1]:
                    point = (point[0], fold[1] - (point[1] - fold[1]))
                fold_set.add(point)

        data = fold_set

    MAX_WIDTH = max(data, key=itemgetter(0))[0]
    MAX_HEIGHT = max(data, key=itemgetter(1))[1]

    image = [['.' for _ in range(MAX_WIDTH + 1)] for _ in range(MAX_HEIGHT + 1)]

    for point in data:
        image[point[1]][point[0]] = '#'

    print(MAX_WIDTH, MAX_HEIGHT)
    for line in image:
        print(line)



def get_input(filename="input.txt"):
    data = set()
    folds = []

    with open(filename, 'r') as f:
        at_fold = False
        for line in f:
            if line == '\n':
                at_fold = True
            elif at_fold:
                axis, val = line[11:].split('=')
                folds.append((axis, int(val[:-1])))
            else:
                row, col = line.split(',')
                data.add((int(row), int(col[:-1])))

    return data, folds


def main():
    print("Part One")
    part_one()

    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
