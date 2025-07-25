def f(x, y):
    return x + y

def rk4(x0, y0, h, xn):
    print("x\t\t y")
    while x0 < xn:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)

        y0 = y0 + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        x0 = x0 + h

        print(f"{x0:.4f}\t {y0:.4f}")

x0 = 0
y0 = 1
h = 0.1
xn = 0.5

rk4(x0, y0, h, xn)
