
def part_one():
    hor_pos = 0
    depth = 0

    with open("input.txt", "r") as f:
        for command in f:
            direction, amount = command.split(" ")
            amount = int(amount)
            if direction == "forward":
                hor_pos += amount
            elif direction == "down":
                depth += amount
            else:
                depth -= amount

    print(hor_pos * depth)


def part_two():
    hor_pos = 0
    depth = 0
    aim = 0

    with open("input.txt", "r") as f:
        for command in f:
            direction, amount = command.split(" ")
            amount = int(amount)
            if direction == "forward":
                hor_pos += amount
                depth += aim * amount
            elif direction == "down":
                aim += amount
            else:
                aim -= amount

    print(hor_pos * depth)


def main():
    print("Part One")
    part_one()
    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
