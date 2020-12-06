
def get_input(filename="input.txt.txt"):
    # Get input.txt from folder
    nums = []
    with open(filename, "r+") as file:
        for line in file:
            nums.append(int(line))

    # Sort numbers so that they are in ascending order
    return sorted(nums)


def get_solution_1a(nums: 'list[int]') -> '(int, int, int)':
    # Start with the lowest and highest element on the list
    i = 0
    k = len(nums) - 1
    while i < k:
        # If the sum is too high, lower the greatest number.
        # If the sum is too low, raise the lowest number.
        # If the sum is just right, return it along with the numbers it added together.
        curr = nums[i] + nums[k]
        if curr == 2020:
            return (nums[i], nums[k], nums[i] * nums[k])
        elif curr < 2020:
            i += 1
        else:
            k -= 1
    return None


def get_solution_1b(nums: 'list[int]') -> '(int, int, int, int)':
    # Set the lowest number. You won't go past len(nums) - 2 since you need two numbers in front of you
    for i in range(len(nums) - 2):
        # Start with the second lowest number and the highest number
        j = i+1
        k = len(nums) - 1
        while j < k:
            # If the sum is too high, lower the greatest number.
            # If the sum is too low, raise the second lowest number.
            # If the sum is just right, return it along with the numbers it added together.
            curr = nums[i] + nums[j] + nums[k]
            if curr == 2020:
                return (nums[i], nums[j], nums[k], nums[i] * nums[j] * nums[k])
            elif curr < 2020:
                j += 1
            else:
                k -= 1


input_list = get_input()
print(get_solution_1a(input_list))
print(get_solution_1b(input_list))
