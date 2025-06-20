import numpy as np

n = int(input("Enter the order of matrix (n): "))
e = float(input("Enter the tolerable error (e): "))

print("Enter the matrix A (row-wise):")
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i+1}][{j+1}]: "))

print("Enter the initial guess vector X:")
X = np.zeros(n)
for i in range(n):
    X[i] = float(input(f"X[{i+1}]: "))

Lambda_Old = 1.0

while True:
    X_NEW = np.zeros(n)
    for i in range(n):
        Temp = 0.0
        for j in range(n):
            Temp += A[i][j] * X[j]
        X_NEW[i] = Temp

    X = X_NEW.copy()

    Lambda_New = abs(X[0])
    for i in range(1, n):
        if abs(X[i]) > Lambda_New:
            Lambda_New = abs(X[i])

    for i in range(n):
        X[i] = X[i] / Lambda_New

    print(f"\nEigenvalue (Lambda_New): {Lambda_New}")
    print("Eigenvector (X):")
    for i in range(n):
        print(f"X[{i+1}] = {X[i]:.6f}")

    if abs(Lambda_New - Lambda_Old) <= e:
        break
    Lambda_Old = Lambda_New

print("\nConverged!")