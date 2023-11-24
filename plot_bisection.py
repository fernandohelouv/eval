import matplotlib.pyplot as plt
import numpy as np


def polynomial_function(x):
    """
    Define a polynomial function.

    Args:
    x (float or array-like): The variable of the polynomial.

    Returns:
    float or array-like: The value of the polynomial at `x`.
    """
    return x**3 - 11 * x**2 + 32 * x - 22


# Generating x values within the range [0, 8] with a total of 400 points for smooth plotting
x_values = np.linspace(0, 8, 400)
# Calculating the corresponding y values using the polynomial function
y_values = polynomial_function(x_values)

# Plotting the polynomial function
plt.plot(x_values, y_values)

# Adding horizontal and vertical lines at y=0 and x=0
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

# Setting the labels for the axes
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)

plt.show()
