def f(x):
 return x**2-4*x-10

while(True):
    x0=int(input("enter a number: "))
    x1=int(input("enter another number in an interval: "))
    if f(x0)*f(x1)>0:
       print("the values are incorrect. please renter another value")
    else:
       break

print("x0\tx1\tx2\tf(x2)")
print("------------------------------")
float_format="{:.3f}"
e=0.001
n=0
while(True):
        x2=(x0+x1)/2
        n=n+1
        if abs(f(x2))<e:
         print("the approximate root is ",x2)
         print("the number of iteration is ",n)
         break
        
        if f(x0)*f(x2)<0:
            x1=x2
        else:
             x0=x2
        print(f"{x0:.3f}\t{x1:.3f}\t{x2:.3f}\t{f(x2):.3f}")
        
            
        