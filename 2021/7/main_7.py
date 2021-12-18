import csv


def part_one():
    data = get_input()
    best_output = -1
    for num in range(min(data), max(data) + 1):
        output = 0
        for i in range(len(data)):
            output += abs(data[i] - num)
        if best_output < 0 or output < best_output:
            best_output = output
        if output > best_output:
            break
    print(best_output)


def part_one_optimized():
    data = get_input()
    output = None
    # pivot = median_of_medians(data)
    for i in range(len(data)):
        output += abs(data[i] - pivot)
    print(output)


def part_two():
    data = get_input()
    best_output = -1
    pivot = 0
    for num in range(min(data), max(data) + 1):
        output = 0
        for i in range(len(data)):
            diff = abs(data[i] - num)
            output += (diff * (diff + 1)) // 2
        if best_output < 0 or output < best_output:
            best_output = output
        if output > best_output:
            break
        pivot = num
    print(best_output)


def part_two_optimized():
    data = get_input()
    avg = sum(data) / len(data)

    best_output = None
    for num in [int(avg), int(avg) + 1]:
        output = 0
        for i in range(len(data)):
            diff = abs(data[i] - num)
            output += (diff * (diff + 1)) // 2
        if best_output is None or best_output > output:
            best_output = output

    print(best_output)


def get_input(filename="test.txt"):
    data = []

    with open(filename, 'r') as f:
        data = next(csv.reader(f))

        for i in range(len(data)):
            data[i] = int(data[i])

    return data


def main():
    print("Part One")
    part_one()
    print("Part One Optimized")
    # part_one_optimized()
    print("Part Two")
    part_two()
    print("Part Two Optimized")
    part_two_optimized()


if __name__ == "__main__":
    main()
