""" This module contains a function to order the numbers of a matrix using the bubble sort algorithm. """


def bubble_sort(matrix: list, verbose: bool = False):
    """This function orders the numbers of a matrix using the bubble sort algorithm.

    Args:
            matrix (list): list of lists of numbers.
    Returns:
            list: list of lists of numbers ordered.
    Test:
            >>> bubble_sort([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """

    # Turn the matrix into a list
    flatten_matrix = [element for row in matrix for element in row]

    # Get the shape of the matrix
    matrix_shape = (len(matrix), len(matrix[0]))

    if verbose:
        print("Flaten matrix:", flatten_matrix)

    # Order the list
    iteration = 0
    swapped = True
    # Loop until there are no more swaps
    while swapped:
        iteration += 1
        swapped = False
        for i in range(len(flatten_matrix) - 1):
            n1 = flatten_matrix[i]
            n2 = flatten_matrix[i + 1]
            # Compare the adjacent numbers and swap them if needed
            if n1 > n2:
                flatten_matrix[i] = n2
                flatten_matrix[i + 1] = n1
                swapped = True
                if verbose:
                    print(f"Iteration [{iteration}]: {flatten_matrix}")
    if verbose:
        print("Ordered List:", flatten_matrix)

    # Turn the ordered list back into a matrix
    ordered_matrix = []
    # Loop through the rows
    for i in range(matrix_shape[0]):
        # Add a new row
        ordered_matrix.append([])
        # Loop through the columns
        for j in range(matrix_shape[1]):
            # Add the element to the row
            ordered_matrix[i].append(flatten_matrix[i * matrix_shape[1] + j])
            if verbose:
                print("Matrix Reconstruction:", ordered_matrix)

    print("Ordered Matrix:", ordered_matrix)
    return ordered_matrix


om = bubble_sort(
    [[9, 8, 7, 5], [4, 5, 6, 10], [3, 2, 1, 8], [5, 6, 7, 9], [1, 2, 3, 5]], True
)
