"This module has functions that prints pyramids of N levels"


# * a)
def print_pyramid(levels: int):
    """
    This function prints out a pyramid of numbers with N levels.
    """
    # The number we start printing from
    current_number = 1

    # Loop through each level
    for level in range(1, levels + 1):
        # Print numbers for the current level
        for _ in range(level):
            print(current_number, end=" ")
            current_number += 1  # Increment the number after printing
        # Move to the next line after each level
        print()


# * b)
def print_pyramid_b(levels: int):
    """
    This function prints a pyramid where each level has numbers in increasing
    order and each row starts with the row number and the numbers increase by 1.
    """

    for i in range(1, levels + 1):
        # Calculate the starting number for this row
        start_num = i
        # Print each number in the row
        for j in range(i):
            print(start_num, end=" ")
            # Increment the number by the first row number
            start_num += i
        # Move to the next line after each level
        print()


# * c)
def print_pyramid_c(levels: int):
    """
    This function prints a pyramid where each level has numbers in increasing
    order and each row starts with the row number and the numbers increase by 2.
    """

    for i in range(1, levels + 1):
        # Calculate the starting number for this row
        start_num = i * 2
        # Print each number in the row
        for j in range(i):
            print(start_num, end=" ")
            # Increment the number by the first row number
            start_num += i * 2
        # Move to the next line after each level
        print()


# * d)
def print_pyramid_d(levels: int):
    """
    This function prints out a pyramid of numbers with N levels.
    Each level has numbers in increasing order up until the level number,
    then the numbers decrease by 1.

    Example:
        1
      1 2 1
    1 2 3 2 1
    """

    # Loop through each level
    for i in range(1, levels + 1):
        # Print spaces for the current level
        for _ in range(levels - i):
            print(" ", end=" ")
        # Print numbers for the current level from 1 up until the level number
        for j in range(1, i + 1):
            print(j, end=" ")
        # Print numbers decreasing from the level number to 1
        for k in range(j - 1, 0, -1):
            print(k, end=" ")
        print()


# * e)
def print_pyramid_e(levels: int):
    """
    This function prints out a pyramid of numbers with (N * 2) - 1 levels.

    Each level has numbers in increasing order up until the level number,
    when the algorithm reaches the N number, it prints the numbers in decreasing order.
    Like a reflected pyramid.

    Example:
    N = 3

    1
    1 2
    1 2 3 <- N number
    1 2
    1
    """

    # Loop through each level and print numbers in increasing order
    for i in range(1, levels + 1):
        # Print numbers for the current level from 1 up until the level number
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # Loop through each level in reverse and print numbers in decreasing order
    for i in range(levels - 1, 0, -1):
        # Print numbers decreasing from the last level number -1 to 1
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# * f)
def print_pyramid_f(levels: int):
    """
    This function prints out a pyramid of numbers with N levels.
    Each level has numbers in increasing order up until the level number,
    then the numbers decrease by 1.

    Example:
         4
       3 2 1
     2  1 0 -1 -2
    1  0 -1 -2 -3 -4
    """
    start = levels

    # Loop through each level
    for i in range(1, levels + 1):
        # Print spaces for the current level
        for _ in range(levels - i):
            print(" ", end=" ")
        # Print numbers for the current level
        row_start = start - (i - 1)
        # print(row_start, end=" ")
        if row_start == levels:
            print(row_start, end=" ")
        elif row_start == levels - 1:
            for j in range(i + 1):
                print(row_start - j, end=" ")
        else:
            for j in range(i + 2):
                print(row_start - j, end=" ")
        print()


#! f')
def print_pyramid_fp(levels: int):
    """
    This function prints out a pyramid of numbers with N levels.
    Each level has numbers in increasing order up until the level number,
    then the numbers decrease by 1.

    Example:
         4
       3 2 1
     2  1 0 -1 -2
    1  0 -1 -2 -3 -4
    """
    start = levels

    # Loop through each level
    for i in range(1, levels + 1):
        # Print spaces for the current level
        for _ in range(levels - i):
            print(" ", end=" ")
        # Print numbers for the current level
        row_start = start - (i - 1)
        for j in range((2 * i) - 1):
            print(row_start - j, end=" ")
        print()


def print_pyramid_by_point(point: str, levels: int):
    """
    Call the appropriate pyramid print function based on the point character.
    Available points are: a, b, c, d, e, f, f'

    Args:
        point (str): The point character
        levels (int): The number of levels for the pyramid
    """
    point_function_map = {
        "a": print_pyramid,
        "b": print_pyramid_b,
        "c": print_pyramid_c,
        "d": print_pyramid_d,
        "e": print_pyramid_e,
        "f": print_pyramid_f,
        "f'": print_pyramid_fp,
    }

    # Check if the inciso is valid and call the corresponding function
    if point in point_function_map:
        point_function_map[point](levels)
    else:
        print("Point not found, available points are: a, b, c, d, e, f, f'")


print_pyramid_by_point("f'", 4)
