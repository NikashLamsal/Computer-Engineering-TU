def f(x):
    return x**3 - 3*x - 2

def regula_falsi(x1, x2, e):
    f1 = f(x1)
    f2 = f(x2)

    if f1 * f2 > 0:
        return "Enter valid values for x1 and x2 (they must bracket the root)"

    while True:
        # Modified formula version
        x0 = (x1 * f2 - x2 * f1) / (f2 - f1)
        f0 = f(x0)

        if abs(f0) < e:
            break

        if f1 * f0 < 0:
            x2 = x0
            f2 = f0
        else:
            x1 = x0
            f1 = f0

    return x0

# Input
x1, x2, e = map(float, input("Enter x1, x2 and e (error tolerance): ").split())
root = regula_falsi(x1, x2, e)
print("Required root:", root)
