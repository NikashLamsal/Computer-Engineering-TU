def f(x):
    return x**3 

def simpsons_38_simple(a, b):
    h = (b - a) / 3
    x1 = a + h
    x2 = a + 2*h
    result = (3 * h / 8) * (f(a) + 3*f(x1) + 3*f(x2) + f(b))
    return result

a = 0
b = 1
print("Simple Simpson's 3/8 Rule result:", simpsons_38_simple(a, b))


# composite

def f(x):
    return x**3  

def simpsons_38_composite(a, b, n):
    if n % 3 != 0:
        raise ValueError("Number of subintervals (n) must be a multiple of 3.")

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            result += 2 * f(x)
        else:
            result += 3 * f(x)

    result *= (3 * h / 8)
    return result


a = 0
b = 1
n = 6  
print("Composite Simpson's 3/8 Rule result:", simpsons_38_composite(a, b, n))
