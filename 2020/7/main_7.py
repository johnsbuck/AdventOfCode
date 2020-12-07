import re
from collections import deque


def get_input(filename="input.txt"):
    output = {}
    with open(filename, "r+") as file:
        for line in file:
            temp = line.rstrip(".\n").replace(" bags", "").replace(" bag", "").split(" contain ")
            key = temp[0]
            rule = temp[1]
            output[key] = []
            if rule != "no other":
                for subrule in rule.split(", "):
                    matches = re.fullmatch(r"^([0-9]+) ([a-z]+ [a-z]+$)", subrule)
                    output[key].append((int(matches.group(1)), matches.group(2)))
    return output


def get_solution_7a(rules: "dict{str: (int, str)}") -> int:
    count = 0
    for rule in rules:
        # Shiny gold bag must be in at least one, so skip
        if rule == "shiny gold":
            continue
        queue = deque([rule])
        visited = set()
        while len(queue) > 0:
            curr = queue.popleft()
            if curr == "shiny gold":
                count += 1
                break
            if curr in visited:
                continue
            for bag in rules[curr]:
                queue.append(bag[1])
            visited.add(curr)
    return count


def get_solution_7b(rules: "dict{str: (int, str)}") -> int:
    # Start at -1 to not count the initial shiny gold bag
    count = -1
    queue = deque([(0, "shiny gold")])
    visited = {}
    while len(queue) > 0:
        curr = queue.pop()
        count += 1
        for bag in rules[curr[1]]:
            for _ in range(bag[0]):
                queue.append(bag)
    return count


data = get_input()
print(get_solution_7a(data))
print(get_solution_7b(data))