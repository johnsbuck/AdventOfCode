from collections import deque


def part_one():
    # Store times it increased
    increased = 0

    # Open input
    with open("input.txt", "r") as f:
        # Get first depth
        prev = int(next(f))

        # Compare each depth from the previous
        for depth in f:
            curr = int(depth)
            increased += prev < curr
            prev = curr

    # Print number of times depth was greater than previous
    print(increased)


def part_two():
    # Store times it increased
    increased = 0

    # Open input
    with open("input.txt", "r") as f:
        window = deque([])
        for _ in range(3):
            window.append(int(next(f)))

        for depth in f:
            curr = int(depth)
            window_sum = sum(window)
            window.popleft()
            window.append(curr)
            increased += window_sum < sum(window)

    print(increased)


def main():
    print("Part One")
    part_one()

    print("Part Two")
    part_two()

if __name__ == "__main__":
    main()
