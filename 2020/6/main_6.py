from collections import Counter


def get_input(filename="input.txt"):
    questions = []
    with open(filename, "r+") as file:
        curr = []
        for line in file:
            if line == "\n":
                questions.append(curr)
                curr = []
            else:
                curr.append(line.rstrip())
        questions.append(curr)
    return questions


def get_solution_6a(groups: "list[list[str]]") -> int:
    count = 0
    for group in groups:
        questions = Counter()
        for person in group:
            questions.update(person)
        count += len(questions)
    return count


def get_solution_6b(groups: "list[list[str]]") -> int:
    count = 0
    for group in groups:
        num_people = len(group)
        questions = Counter()
        for person in group:
            questions.update(person)
        for quest in questions.most_common():
            if quest[1] == num_people:
                count += 1
            else:
                break
    return count


groups = get_input()
print(get_solution_6a(groups))
print(get_solution_6b(groups))
