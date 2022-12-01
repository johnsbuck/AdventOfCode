import re


def part_one():
    data = get_input()
    print(sum(range(abs(data[2]))))


def part_two():
    data = get_input()

    output = set()

    for x_vel in range(1, data[1] + 1):
        for y_vel in range(data[2], abs(data[2])):
            pos = [0, 0]
            initial = (x_vel, y_vel)

            # Stupid Python, referencing my integers
            test_x = x_vel
            test_y = y_vel

            while pos[0] <= data[1] and pos[1] >= data[2]:
                pos = [pos[0] + test_x, pos[1] + test_y]

                if test_x != 0:
                    test_x -= 1
                test_y -= 1

                if data[0] <= pos[0] <= data[1] and data[2] <= pos[1] <= data[3]:
                    output.add(initial)
                    break

    print(len(output))


def get_input(filename="input.txt"):
    data = []

    with open(filename, 'r') as f:
        data = [int(x) for x in re.findall(r'(-?\d+)', f.read())]

    return data


def main():
    print("Part One")
    part_one()

    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
