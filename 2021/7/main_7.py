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
    output = 0
    pivot = select(data, len(data)//2)
    for i in range(len(data)):
        output += abs(data[i] - pivot)
    print(output)


# Taken from Stack Overflow
# (https://stackoverflow.com/questions/10806303/python-implementation-of-median-of-medians-algorithm)
def select(L, j):
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        Meds.append(select(subList, int((len(subList)-1)/2)))
    med = select(Meds, int((len(Meds)-1)/2))
    L1 = []
    L2 = []
    L3 = []
    for i in L:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    if j < len(L1):
        return select(L1, j)
    elif j < len(L2) + len(L1):
        return L2[0]
    else:
        return select(L3, j-len(L1)-len(L2))


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
    part_one_optimized()
    print("Part Two")
    part_two()
    print("Part Two Optimized")
    part_two_optimized()


if __name__ == "__main__":
    main()
