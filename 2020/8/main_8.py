from typing import Union


def get_input(filename="input.txt"):
    output = []
    with open(filename, "r+") as file:
        for line in file:
            output.append(line.rstrip().split(" "))
            output[-1][1] = int(output[-1][1])
    return output


def get_solution_8a(instructions: "list[[str, int]]") -> int:
    # Create boolean list to determine if instruction has been previously read
    visited = [False for _ in range(len(instructions))]
    # Create indexing variable
    idx = 0
    # Create global accumulator variable
    acc = 0

    # Keep running the program until we visit a instruciton twice
    while not visited[idx]:
        visited[idx] = True
        jmp = 1
        # Accumulator Instruction
        if instructions[idx][0] == "acc":
            acc += instructions[idx][1]
        # Jumping Instruction
        elif instructions[idx][0] == "jmp":
            jmp = instructions[idx][1]
        idx += jmp
    return acc


def get_solution_8b(instructions: "list[[str, int]]") -> int:

    visited = [False for _ in range(len(instructions))]
    return traversal(instructions, visited)


def traversal(instructions: "list[[str, int]]",
              visited: "list[bool]", idx=0, acc=0, changed=False) -> Union[None, int]:
    # If program reaches end, return accumulator
    if idx == len(instructions):
        return acc

    # If visited, return None as instruction is invalid
    if visited[idx]:
        return None

    # Get command string & value, and set visited to true for instruction index
    command, value = instructions[idx]
    visited[idx] = True

    # If acc, run as normal
    if command == "acc":
        output = traversal(instructions, visited, idx+1, acc+value, changed)
        if output is not None:
            return output
    elif command == "jmp":
        # If a change has already been made, run as normal
        if changed:
            output = traversal(instructions, visited, idx+value, acc, changed)
            if output is not None:
                return output
        else:
            # A change has not been made.
            # Attempt to make change and if None is returned, try original jmp
            output = traversal(instructions, visited, idx+1, acc, True)
            if output is not None:
                return output
            else:
                output = traversal(instructions, visited, idx + value, acc, changed)
                if output is not None:
                    return output
    else:
        # If a change has already been made, run as normal
        if changed:
            output = traversal(instructions, visited, idx+1, acc, changed)
            if output is not None:
                return output
        else:
            # A change has not been made.
            # Attempt to make change and if None is returned, try original nop
            output = traversal(instructions, visited, idx + value, acc, True)
            if output is not None:
                return output
            else:
                output = traversal(instructions, visited, idx+1, acc, changed)
                if output is not None:
                    return output
    visited[idx] = False
    return None


instructions = get_input()
print(get_solution_8a(instructions))
print(get_solution_8b(instructions))
