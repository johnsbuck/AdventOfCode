""" Advent of Code 2023 - Problem 7 (https://adventofcode.com/2023/day/7)
"""
from typing import List
from collections import Counter


def get_input(filename: str = "input.txt") -> List[List[str]]:
    """Retrieve file input from Advent of Code (expected to be csv)

        Arguments:
            filename (str): The text file to input. (Default: "input.txt")
            conv_type (type): The python type to convert the data to. (Default: int)

        Returns:
            (list(conv_type)) A list of inputs formatted to the given python type.
        """
    data = []

    with open(filename, 'r') as f:
        for row in f:
            data.append(row.split(' '))
            data[-1][1] = int(data[-1][1])
    return data

def part_one(filename: str = "input.txt"):
    """ First part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 1 Solution
        """
    CARD_ORD = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    CARD_STR = {CARD_ORD[i]: i for i in range(len(CARD_ORD))}
    HAND_STR = {(1, 1, 1, 1, 1): 0, # High Card
                (2, 1, 1, 1): 1,    # One Pair
                (2, 2, 1): 2,       # Two Pair
                (3, 1, 1): 3,       # Three of a Kind
                (3, 2): 4,          # Full House
                (4, 1): 5,          # Four of a Kind
                (5,): 6}            # Five of a Kind
    STR_CARD = {v: k for k, v in CARD_STR.items()}

    data = get_input(filename)

    # Get Hand Strengths
    hands = []
    for i in range(len(data)):
        count = Counter(data[i][0])
        hand = tuple(y for _, y in count.most_common())
        strength = tuple([HAND_STR[hand]] + [CARD_STR[c] for c in data[i][0]])
        hands.append([strength, i])
    hands.sort()

    # Get Total Winnings
    output = 0
    for i in range(len(hands)):
        bet = data[hands[i][1]][1] * (i+1)
        output += bet
    return output

def part_two(filename: str = "input.txt"):
    """ Second part of problem

        Arguments:
            filename (str): The text file with problem input. (Default: "input.txt")

        Returns:
            (int) Part 2 Solution
        """
    CARD_ORD = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    CARD_STR = {CARD_ORD[i]: i for i in range(len(CARD_ORD))}
    HAND_STR = {(1, 1, 1, 1, 1): 0,  # High Card
                (2, 1, 1, 1): 1,  # One Pair
                (2, 2, 1): 2,  # Two Pair
                (3, 1, 1): 3,  # Three of a Kind
                (3, 2): 4,  # Full House
                (4, 1): 5,  # Four of a Kind
                (5,): 6}  # Five of a Kind
    STR_CARD = {v: k for k, v in CARD_STR.items()}

    data = get_input(filename)

    # Get Hand Strengths
    hands = []
    for i in range(len(data)):
        # Get best hand w/ wildcards
        strong_hand = sorted(data[i][0], key=lambda x: CARD_STR[x], reverse=True)
        count = Counter(strong_hand)
        mcc = count.most_common(2)
        if len(mcc) > 1:
            if mcc[0][0] == 'J':
                count[mcc[1][0]] += count['J']
            else:
                count[mcc[0][0]] += count['J']
            del count['J']

        # Get hand strength w/ card strengths
        hand = tuple(y for _, y in count.most_common())
        strength = tuple([HAND_STR[hand]] + [CARD_STR[c] for c in data[i][0]])
        hands.append([strength, i])
    hands.sort()

    # Get Total Winnings
    output = 0
    for i in range(len(hands)):
        bet = data[hands[i][1]][1] * (i + 1)
        output += bet
    return output


if __name__ == "__main__":
    print("Advent of Code - 2023 - Problem 7")
    print("----------------------------------")
    print(part_one())
    print("EOP")
    print()
    print(part_two())
    print("EOP")
