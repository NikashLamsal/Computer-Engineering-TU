def f(x):
    ans = x**3 - 3*x -2
    return ans

def regula_falsi(x1, x2, e):
    f1 = f(x1)
    f2 = f(x2)
    x0 = x1
    if f1*f2 > 0:
        ans = "Enter valid value for x1 and x2"
        return ans

    while(True):
        x0 = (x1*f(x2)-x2*f(x2))/(f(x2)-f(x1))
       # x0 = x1 - f1 * (x2 - x1) / (f2 - f1)

        f0 = f(x0)

        if abs(f0) < e:
            break        

        if (f1*f0) < 0:
            x2, f2 = x0, f0
        else:
            x1, f1 = x0, f0
            
    return x0

x1, x2, e = map(float, input("Enter x2, x2 and e:"))
root = regula_falsi(x1, x2, e)
print("Required root: ",root)
