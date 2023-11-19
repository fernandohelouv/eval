"""
This module contains a function to find perfect numbers within a given range.
"""


def perfect_nums(first: int, last: int):
    """
    Find perfect numbers within the given range.

    Args:
            first (int): The starting number of the range.
            last (int): The ending number of the range.

    Returns:
            list: A list of perfect numbers within the given range.

    Test:
        >>> perfect_nums(1, 10)
        [6]
    """
    perfect_numbers = []
    # Loop through the range of numbers
    for i in range(first, last):  # 6
        divisors = []
        # Loop from one to half of the number + 1 of each number to get its divisors
        for j in range(1, i // 2 + 1):  # 1, 2, 3, 4 for efficiency
            if i % j == 0:
                # 6 % 1 == 0, 6 % 2 == 0, 6 % 3 == 0, 6 % 4 == 2, 6 % 5 == 1, 6 % 6 == 0
                divisors.append(j)  # [1, 2, 3, 6]
        # Check if the sum of the divisors is equal to the number
        if sum(divisors) == i:  # 12 - 6 == 6
            perfect_numbers.append(i)
    return perfect_numbers


print(perfect_nums(1, 10000))
