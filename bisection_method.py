" The bisection method is a root-finding algorithm that repeatedly bisects an interval and then selects a subinterval in which a root must lie for further processing. "


def bisection_method(f, a, b, tolerance=1e-6, max_iterations=1000) -> float:
    """
    Find a root of the function `f` within the interval [a, b] using the bisection method.

    Args:
    f (callable): The function for which the root is to be found.
    a (float): The starting point of the interval.
    b (float): The ending point of the interval.
    tolerance (float): The accuracy of the approximation of the root.
    max_iterations (int): The maximum number of iterations to perform.

    Returns:
    float: An approximation of the root of `f`.

    Raises:
    ValueError: If `f(a)` and `f(b)` have the same sign, indicating no root in [a, b].
    """
    fa = f(a)  # Evaluate the function at the starting point.
    fb = f(b)  # Evaluate the function at the ending point.

    if fa * fb > 0:
        raise ValueError(
            "Function must have opposite signs at a and b to apply the bisection method."
        )

    for _ in range(max_iterations):
        m = (a + b) / 2  # Compute the midpoint of the interval.
        fm = f(m)  # Evaluate the function at the midpoint.

        if (
            abs(fm) < tolerance or (b - a) / 2 < tolerance
        ):  # Check if the root has been found.
            return m  # Return the midpoint.

        if fa * fm < 0:  # Check if the root is in the first half of the interval.
            b = m  # Update the ending point of the interval.
            fb = fm  # Update the value of the function at the ending point.
        else:  # The root is in the second half of the interval.
            a = m  # Update the starting point of the interval.
            fa = fm  # Update the value of the function at the starting point.

    return (a + b) / 2  # Return the midpoint of the interval.


def polynomial_function(x):
    """
    Define a polynomial function.

    Args:
    x (float): The variable of the polynomial.

    Returns:
    float: The value of the polynomial at `x`.
    """
    return x**3 - 11 * x**2 + 32 * x - 22


# Applying the bisection method to find the remaining roots in different intervals.
# We use [0, 3] and [3, 6] to search for the other two roots, as we know one is around 6.732.
try:
    root_bisection_interval_1 = bisection_method(polynomial_function, 0, 3)
except ValueError as e:
    root_bisection_interval_1 = "Error: " + str(e)

try:
    root_bisection_interval_2 = bisection_method(polynomial_function, 3, 6)
except ValueError as e:
    root_bisection_interval_2 = "Error: " + str(e)

try:
    root_bisection_interval_3 = bisection_method(polynomial_function, 6, 8)
except ValueError as e:
    root_bisection_interval_3 = "Error: " + str(e)


# Print the roots found in the specified intervals.
print("root 1: ", root_bisection_interval_1)
print("test 1: ", polynomial_function(root_bisection_interval_1))
print("root 2: ", root_bisection_interval_2)
print("test 2: ", polynomial_function(root_bisection_interval_2))
print("root 3: ", root_bisection_interval_3)
print("test 3: ", polynomial_function(root_bisection_interval_3))
