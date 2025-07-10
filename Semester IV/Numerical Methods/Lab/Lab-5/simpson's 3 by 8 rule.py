def f(x):
    return 1 + x**3

def simpson_38(x, y, n):
    if n % 3 != 0:
        print("Number of subintervals must be a multiple of 3 for Simpson's 3/8 rule.")
        return None

    h = (y - x) / n
    result = f(x) + f(y)

    for i in range(1, n):
        k = x + i * h
        if i % 3 == 0:
            result += 2 * f(k)
        else:
            result += 3 * f(k)

    result *= (3 * h / 8)
    return result

low = 1
up = 3
sub = 6  

result = simpson_38(low, up, sub)
if result is not None:
    print(f"Result = {result}")
