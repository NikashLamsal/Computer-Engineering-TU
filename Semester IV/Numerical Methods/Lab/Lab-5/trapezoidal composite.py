import numpy as np

def composite_trapezoidal(a, b, n, f):
    h = (b - a) / n
    I = h / 2 * (f(a) + f(b))
    for i in range(1, n):
        I += h * f(a + i * h)
    return I

if __name__ == "__main__":
    def f(x): 
        return x**2

    a_composite = 0
    b_composite = 2
    n = 4

    result_composite = composite_trapezoidal(a_composite, b_composite, n, f)
    print(f"Composite Trapezoidal Rule result (n={n}): {result_composite}")
