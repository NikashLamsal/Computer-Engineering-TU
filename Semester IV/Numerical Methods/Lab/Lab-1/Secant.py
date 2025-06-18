import math
def func(x):
    return x**2-4*x-10
x0=float(input("enter first intial guess:"))
x1=float(input("enter second initial guess:"))
e=float((input("enter tolerable error")))
n=int(input("enter the no of steps"))
while(func(x0)*func(x1)>0):
    print("you have given wrong initial guess ")
    print("take another inputs")
    x0=float(input("enter first intial guess:"))
    x1=float(input("enter second initial guess:"))
print("\nstep\t\tx0\t\tx1\t\tx2\t\tf(x2)")
step=1
condition=True
while condition:
    if step>n:
        print("not convergent. The value of root calculated upto now is as below")
        break
    x2=(x0*func(x1)-x1*func(x0))/func(x1)-func(x0)
    f2=func(x2)
    print(step,"\t\t""%.4f"%x0,"\t\t""%0.4f"%x1,"\t\t""%0.4f"%x2,"\t\t""%0.4f"%f2)
    condition=math.fabs(f2)
    x0=x1
    x1=x2
    step+=1
print("the value of root is :","%.4f"%x2)

