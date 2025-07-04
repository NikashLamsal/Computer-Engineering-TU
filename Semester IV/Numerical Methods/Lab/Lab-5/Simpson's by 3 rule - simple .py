import numpy as np

def simpson_one_third(a, b, fa, fab, fb):
    h = (b - a) / 2
    I = h / 3 * (fa + 4 * fab + fb)
    return I

if __name__ == "__main__":
    def f(x):
        return x**2
    
    a = 0
    b = 2
    fa = f(a)
    fab = f((a + b) / 2)
    fb = f(b)
    result = simpson_one_third(a, b, fa, fab, fb)
    print(f"Simpson's 1/3 Rule result: {result}")