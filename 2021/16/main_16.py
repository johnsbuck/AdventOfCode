
def part_one():
    data = get_input()

    output, data = packet_parser(data)

    print(output)


def packet_parser(data):
    output = 0

    while len(data) > 0:
        print(data)
        packet_version = int(data[:3], 2)
        data = data[3:]
        output += packet_version

        type_id = int(data[:3], 2)
        data = data[3:]

        # print(packet_version, type_id, output, len(data))

        if type_id == 4:
            last_group = False
            while not last_group:
                if data[0] == '0':
                    last_group = True
                data = data[5:]
        else:
            length_type_id = int(data[0])
            data = data[1:]
            if length_type_id == 0:
                packet_length = int(data[:15], 2)
                data = data[15:]
                sub_packets = data[:packet_length]
                data = data[packet_length:]
                temp, data = packet_parser(data)
                output += temp
            elif length_type_id == 1:
                packet_length = int(data[:11], 2)
                data = data[11:]
                temp, data = packet_parser(data)
                output += temp

    return output, data


def part_two():
    pass


def get_input(filename="test.txt"):
    data = ""

    with open(filename, 'r') as f:
        for line in f:
            for c in line[:-1]:
                data += format(int(c, 16), "04b")

    return data


def main():
    print("Part One")
    part_one()

    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
