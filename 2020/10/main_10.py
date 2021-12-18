
def get_input(filename="input.txt"):
    output = []
    with open(filename, "r+") as file:
        for line in file:
            output.append(line.rstrip())
    return output


print(get_input())
