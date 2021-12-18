import csv


def part_one():
    data = get_input()

    # Cycle for 80 days
    for i in range(80):
        # Range of starting day length
        for k in range(len(data)):
            if data[k] == 0:
                data.append(8)
                data[k] = 6
            else:
                data[k] -= 1

    print(len(data))


def part_two():
    data = get_input()

    # Create dict for each day of lanternfish breeding
    days = {x: 0 for x in range(0, 9)}

    # Add a fish for each breeding day
    for fish in data:
        days[fish] += 1

    # Cycle for 256 days
    for i in range(256):
        # Shift days down
        new_days = {x: 0 for x in range(0, 9)}
        for k in range(8, -1, -1):
            # If a lanternfish is at their final day, move them to 6 and add the new lanternfish to 8
            if k == 0:
                new_days[8] += days[k]
                new_days[6] += days[k]
            # Else, shift lanternfish down one day
            else:
                new_days[k-1] = days[k]
        days = new_days

    # Add all laternfish to output
    output = 0

    for k in days:
        output += days[k]

    print(output)


def get_input(filename="input.txt"):
    data = []

    with open(filename, 'r') as f:
        data = next(csv.reader(f))
        for i in range(len(data)):
            data[i] = int(data[i])

    return data


def main():
    print("Part One")
    part_one()
    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
