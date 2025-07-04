import numpy as np

def simple_trapezoidal(a, b, fa, fb):
    h = b - a
    I = h / (2 * (fa + fb))
    return I

if __name__ == "__main__":
    def f(x):
        return x**2
    
    a_simple = 0
    b_simple = 2
    fa = f(a_simple)
    fb = f(b_simple)
    result_simple = simple_trapezoidal(a_simple, b_simple, fa, fb)
    print(f"Simple Trapezoidal Rule result: {result_simple}")
