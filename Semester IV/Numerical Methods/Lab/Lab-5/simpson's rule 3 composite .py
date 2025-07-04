import numpy as np

def composite_simpson_one_third(a, b, n, f):
    if n % 2 != 0:
        n += 1  
    h = (b - a) / n
    I = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            I += 2 * f(a + i * h)
        else:
            I += 4 * f(a + i * h)
    I *= h / 3
    return I

if __name__ == "__main__":
    def f(x):
        return x**2
    
    a = 0
    b = 2
    n = 4
    result = composite_simpson_one_third(a, b, n, f)
    print(f"Composite Simpson's 1/3 Rule result (n={n}): {result}")