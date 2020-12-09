from collections import deque
from typing import Union


def get_input(filename="input.txt"):
    output = []
    with open(filename, "r+") as file:
        for line in file:
            output.append(int(line.rstrip()))
    return output


def get_solution_9a(code: "list[int]") -> Union[int, None]:
    preamble = deque(code[:25])
    code = code[25:]
    for num in code:
        # Sort the previous 25 numbers to better find the sum
        # Note: You can do an initial sort of indices based on preamble values outside of the for loop and do a
        # binary insertion for a O(logn) instead of this O(nlogn) each cycle.
        sort_amble = sorted(preamble)

        # Start with the lowest and highest values in the preamble
        i = 0
        k = len(sort_amble) - 1
        curr = sort_amble[i] + sort_amble[k]

        # While the two indices have not cross, try to find a matching sum for the number
        while i < k:
            if curr == num:
                break
            if curr > num:
                k -= 1
            else:
                i += 1
            curr = sort_amble[i] + sort_amble[k]

        # If no match is found, return the number from the file
        if curr != num:
            return num
        # Match is not found, add number to preamble and remove the earliest number
        preamble.popleft()
        preamble.append(num)

    # No match is found, return None
    return None


def get_solution_9b(code: "list[int]") -> Union[int, None]:
    # Get invalid number
    invalid_num = get_solution_9a(code)

    # Start continuous set
    cont_set = deque()
    # Store total for easier use and not having to use the sum function
    total = 0

    for num in code:
        # While the set is too large of sum, remove the earliest number from the set
        while total > invalid_num:
            total -= cont_set.popleft()
        # Match found, return sum of minimum and maximum number in set
        if total == invalid_num:
            return min(cont_set) + max(cont_set)
        # Total sum is too low, add most newest number
        if total < invalid_num:
            total += num
            cont_set.append(num)

    # No match is found, return None
    return None


file_data = get_input()
print(get_solution_9a(file_data))
print(get_solution_9b(file_data))
