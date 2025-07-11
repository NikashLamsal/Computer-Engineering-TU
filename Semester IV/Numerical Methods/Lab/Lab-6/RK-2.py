def f(x,y):
    return 3*x*x + 1

x0 = float(input("Enter initial value of x: "))
y0 = float(input("Enter initial value of y: "))
xp = float(input("Enter the value of x whose functional value is to be approximated: "))
h = float(input("Enter the step-size: "))
#n = (xp - x0)/h
while(x0!=xp):

    y0 = y0 + (h/2) * (f(x0,y0) +f(x0+h,y0+h*f(x0,y0)))
    x0 = x0 + h
print(f"The functional value at x = {xp} is: {y0}")