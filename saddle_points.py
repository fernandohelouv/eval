" This module contains tow functions to find saddle points in a matrix. "


def saddle_points(matrix: list):
    """
    Find saddle points in a matrix.

    Args:
        matrix (list): The matrix to find saddle points in.

    Returns:
        list: A list of saddle points in the matrix.

    Test:
        >>> saddle_point([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [(0, 2)]
    """

    sadd_p = []
    # Loop through the matrix
    for i, row in enumerate(matrix):
        # print(i, row, min(row))
        min_value = min(row)
        for j, column in enumerate(zip(*matrix)):
            # print(j, column, max(column))
            max_value = max(column)
            if min_value == max_value:
                sadd_p.append((i, j))

    return sadd_p


def saddle_points_values(matrix: list, s_p: list):
    """
    Find saddle points values in a matrix.

    Args:
            matrix (list): The matrix to find saddle points in.
            s_p (list): The list of saddle points.

    Returns:
            list: A list of saddle points values in the matrix.

    Test:
            >>> saddle_points_values([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [(2, 0)])
            [7]
    """
    if len(s_p) == 0:
        return "There are no saddle points in the matrix."
    sp_values = []
    for i, j in s_p:
        sp_values.append(matrix[i][j])

    return f"The saddle points in the matrix {matrix} are {s_p} with values {sp_values}"


mtx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sp = saddle_points(mtx)
sp_v = saddle_points_values(mtx, sp)
print(sp_v)

mtx = [[2, 8, 7], [5, 9, 6], [2, 6, 7]]
sp = saddle_points(mtx)
sp_v = saddle_points_values(mtx, sp)
print(sp_v)

mtx = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
sp = saddle_points(mtx)
spv = saddle_points_values(mtx, sp)
print(spv)
