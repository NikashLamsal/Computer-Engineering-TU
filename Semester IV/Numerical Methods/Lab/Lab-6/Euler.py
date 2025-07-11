def eulerm(x,y):
    return 1 + 3*x*x

x0 = float(input("enter the initial guess x :"))
y0 = float(input("enter the initial guess y :"))
h = float(input("enter the step size :"))
xn = float(input("enter the value of xn :"))


def euler(x0,y0,xn,h):
    n = round((xn - x0)/h)
    print("\n x\t\t y\t\t m\t\t y_next")
    for i in range(n):
        m = eulerm(x0,y0)
        yn = y0 + m + h
        y0 = yn
        x0 = x0 + h
    print("\nAt x = %.4f, y = %.4f (approx)" % (x0, y0))

euler(x0, y0, xn, h)
