
def part_one():
    bits = []
    length = 0

    with open("input.txt", "r") as f:
        # Ignore last character (\n)
        bits = [int(x) for x in next(f)[:-1]]
        length += 1

        for num in f:
            # Ignore last character (\n)
            for i in range(len(num) - 1):
                bits[i] += int(num[i])
            length += 1

    gamma = ""
    epsilon = ""
    for bit in bits:
        if bit > length // 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(gamma, "*", epsilon, "=", gamma * epsilon)


def part_two():
    nums = []
    one_count = 0
    mask = 1 << 11

    # Get list of numbers and find most common first bit
    with open("input.txt", "r") as f:
        for num in f:
            # Ignore last character (\n)
            nums.append(int(num[:-1], 2))

            # Get number of ones in first bit position of each number
            one_count += nums[-1] & mask > 0

    # Get initial list for oxygen rate and CO2 Scruber Rate
    oxygen_rate_list = []
    scrubber_rate_list = []

    most_common_bit = one_count >= len(nums) // 2
    while len(nums) > 0:
        x = nums.pop()
        if x & mask > 0:
            if most_common_bit:
                oxygen_rate_list.append(x)
            else:
                scrubber_rate_list.append(x)
        else:
            if most_common_bit:
                scrubber_rate_list.append(x)
            else:
                oxygen_rate_list.append(x)

    # Get Oxygen Rate Number
    mask = 1 << 10
    while mask > 0 and not len(oxygen_rate_list) == 1:
        oxy_one_count = 0
        for num in oxygen_rate_list:
            oxy_one_count += num & mask > 0

        oxy_state = 2 if oxy_one_count * 2 == len(oxygen_rate_list) else oxy_one_count * 2 > len(oxygen_rate_list)

        new_list = []
        for num in oxygen_rate_list:
            if oxy_state == 0:
                if num & mask == 0:
                    new_list.append(num)
            else:   # oxy_state == 1 or oxy_state == 2
                if num & mask > 0:
                    new_list.append(num)
        mask >>= 1
        oxygen_rate_list = new_list
    oxygen_rate = oxygen_rate_list[0]

    # Get CO2 Scrubber Rate Number
    mask = 1 << 10
    while mask > 0 and not len(scrubber_rate_list) == 1:
        scrubber_one_count = 0
        for num in scrubber_rate_list:
            scrubber_one_count += num & mask > 0

        scrubber_state = 2 if scrubber_one_count * 2 == len(scrubber_rate_list) else scrubber_one_count * 2 > len(scrubber_rate_list)

        new_list = []
        for num in scrubber_rate_list:
            if scrubber_state == 0:
                if num & mask > 0:
                    new_list.append(num)
            else:   # scrubber_state == 1 or 2
                if num & mask == 0:
                    new_list.append(num)
        mask >>= 1
        scrubber_rate_list = new_list

    scrubber_rate = scrubber_rate_list[0]
    print(oxygen_rate, bin(oxygen_rate), scrubber_rate, bin(scrubber_rate), oxygen_rate * scrubber_rate)


def main():
    print("Part One")
    part_one()

    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
