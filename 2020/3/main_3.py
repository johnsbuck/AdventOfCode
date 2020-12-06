

def get_input(filename="input.txt.txt"):
    with open(filename) as file:
        patterns = [x.rstrip() for x in file.readlines()]
    return patterns


def get_solution_3a(patterns: 'list[str]') -> int:
    k = 0
    count = 0
    for i in range(1, len(patterns)):
        k = (k + 3) % len(patterns[0])
        count += patterns[i][k] == '#'
    return count

def get_solution_3b(patterns: 'list[str]') -> int:
    total = 1
    for inc in [1, 3, 5, 7]:
        k = 0
        count = 0
        for i in range(1, len(patterns)):
            k = (k + inc) % len(patterns[0])
            count += patterns[i][k] == '#'
        total *= count

    k = 0
    count = 0
    for i in range(2, len(patterns), 2):
        k = (k + 1) % len(patterns[0])
        count += patterns[i][k] == "#"
    return total * count


print(get_solution_3b(get_input()))
