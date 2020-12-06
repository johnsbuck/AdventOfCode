import re


def get_input(filename="input.txt.txt"):
    with open(filename, 'r+') as file:
        pass_check = []
        for line in file:
            new_pass = re.split(" |-|: ", line.rstrip())
            new_pass[0] = int(new_pass[0])
            new_pass[1] = int(new_pass[1])
            pass_check.append(new_pass)
        return pass_check


def get_solution_2a(passwords: 'list[(int, int, str, str)]') -> int:
    return sum(x[0] <= x[3].count(x[2]) <= x[1] for x in passwords)


def get_solution_2b(passwords: 'list[(int, int, str, str)]') -> int:
    return sum((x[3][x[0]-1] == x[2]) ^ (x[3][x[1]-1] == x[2]) for x in passwords)


print(get_solution_2a(get_input()))
print(get_solution_2b(get_input()))