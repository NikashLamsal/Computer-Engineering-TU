import numpy as np

n = int(input("Enter the order of the matrix (n): "))
print(f"Enter the augmented matrix A ({n}x{n+1}, row-wise):")
A = np.zeros((n, n+1), dtype=float)
for i in range(n):
    for j in range(n+1):
        A[i][j] = float(input(f"A[{i+1}][{j+1}]: "))

for i in range(n-1):
    if A[i][i] == 0:
        print("Mathematical Error! Pivot is zero.")
        exit()
    for j in range(i+1, n):
        Ratio = A[j][i] / A[i][i]
        for k in range(n+1):
            A[j][k] = A[j][k] - Ratio * A[i][k]

if A[n-1][n-1] == 0:
    print("Mathematical Error! Final pivot is zero.")
    exit()

X = np.zeros(n, dtype=float)
X[n-1] = A[n-1][n] / A[n-1][n-1]
for i in range(n-2, -1, -1):
    X[i] = A[i][n]
    for j in range(i+1, n):
        X[i] = X[i] - A[i][j] * X[j]
    X[i] = X[i] / A[i][i]

print("\nSolution:")
for i in range(n):
    print(f"X[{i+1}] = {X[i]:.6f}")

print("Program completed.")