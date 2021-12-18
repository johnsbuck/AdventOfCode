from collections import Counter


def part_one():
    data = get_input()

    for _ in range(10):
        new_poly = ""
        for i in range(len(data[0]) - 1):
            char = None
            found = False
            for rule in data[1]:
                if rule == data[0][i:i+2]:
                    found = True
                    char = data[1][rule]
                    break

            new_poly += data[0][i]
            if found:
                new_poly += char
        data[0] = new_poly + data[0][-1]

    count = Counter(data[0])
    print(count.most_common()[0][1] - count.most_common()[-1][1])


def part_two():
    data = get_input()

    pairs = {}

    last_char = data[0][-1]

    for i in range(len(data[0]) - 1):
        seq = data[0][i:i+2]
        if seq in pairs:
            pairs[seq] += 1
        else:
            pairs[seq] = 1

    for step in range(40):
        new_pairs = {}

        for seq in list(pairs.keys()):
            if seq in data[1]:
                left_key = seq[0] + data[1][seq]
                right_key = data[1][seq] + seq[1]

                if left_key in new_pairs:
                    new_pairs[left_key] += pairs[seq]
                else:
                    new_pairs[left_key] = pairs[seq]

                if right_key in new_pairs:
                    new_pairs[right_key] += pairs[seq]
                else:
                    new_pairs[right_key] = pairs[seq]
                del pairs[seq]

        for seq in pairs:
            if seq in new_pairs:
                new_pairs[seq] += pairs[seq]
            else:
                new_pairs[seq] = pairs[seq]

        pairs = new_pairs

    count = Counter([])

    for seq in pairs:
        # Take first letter of each sequence
        count += Counter({seq[0]: pairs[seq]})
    count += Counter([last_char])

    # Print out difference
    print(count.most_common()[0][1] - count.most_common()[-1][1])


def get_input(filename="input.txt"):
    data = []
    with open(filename, 'r') as f:
        is_rules = False
        for line in f:
            if line == '\n':
                is_rules = True
                data.append({})
            elif not is_rules:
                data.append(line[:-1])
            else:
                line = line[:-1].split(' -> ')
                data[1][line[0]] = line[1]

    return data


def main():
    print("Part One")
    part_one()

    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
