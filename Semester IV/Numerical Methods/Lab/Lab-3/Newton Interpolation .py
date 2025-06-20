import numpy as np
import math

# Function to calculate factorial
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Function to construct forward difference table
def forward_difference_table(y, n):
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    return diff_table

# Function to perform Newton Forward Interpolation
def newton_forward(x, y, value):
    n = len(x)
    h = x[1] - x[0]
    u = (value - x[0]) / h

    diff_table = forward_difference_table(y, n)

    # Display forward difference table
    print("\nForward Difference Table:")
    for i in range(n):
        print(f"{x[i]:.2f}", end="\t")
        for j in range(n - i):
            print(f"{diff_table[i][j]:.4f}", end="\t")
        print()

    # Calculating the interpolation value
    result = y[0]
    for i in range(1, n):
        term = diff_table[0][i]
        for j in range(i):
            term *= (u - j)
        result += term / factorial(i)

    return result

# --- Main Program ---
n = int(input("Enter number of data points: "))
x = np.zeros(n)
y = np.zeros(n)

print("Enter x and y values:")
for i in range(n):
    x[i] = float(input(f"x[{i}] = "))
    y[i] = float(input(f"y[{i}] = "))

value = float(input("Enter the value of x to interpolate: "))

# Perform interpolation
interp_value = newton_forward(x, y, value)
print(f"\nInterpolated value at x = {value} is {interp_value:.4f}")
