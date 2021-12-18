
def part_one():
    data = get_input()

    SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
    ENDS_PAIR = {'(': ')', '[': ']', '{': '}', '<': '>'}

    output = 0

    for line in data:
        stack = []
        for c in line:
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            elif ENDS_PAIR[stack[-1]] != c:
                output += SCORES[c]
                break
            else:
                stack.pop()

    print(output)


def part_two():
    data = get_input()

    PAREN_SCORES = {'(': 1, '[': 2, '{': 3, '<': 4}
    ENDS_PAIR = {'(': ')', '[': ']', '{': '}', '<': '>'}

    all_scores = []

    for line in data:
        stack = []
        valid = True
        for c in line:
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            elif ENDS_PAIR[stack[-1]] != c:
                valid = False
                break
            else:
                stack.pop()

        if valid:
            score = 0
            while len(stack) > 0:
                c = stack.pop()
                score *= 5
                score += PAREN_SCORES[c]
            all_scores.append(score)

    all_scores.sort()
    print(all_scores[len(all_scores) // 2])


def get_input(filename="input.txt"):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append([])
            for c in line:
                if c == '\n':
                    continue
                data[-1].append(c)
    return data


def main():
    print("Part One")
    part_one()
    print("Part Two")
    part_two()


if __name__ == "__main__":
    main()
