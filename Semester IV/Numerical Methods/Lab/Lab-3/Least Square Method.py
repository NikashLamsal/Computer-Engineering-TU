import numpy as np
import matplotlib.pyplot as plt  # Importing matplotlib

n = int(input('Enter number of data points: '))
x = np.zeros((n))
y = np.zeros((n))
sxy = 0
sx = 0
sy = 0
sx2 = 0

print('Enter data for x and y:')
for i in range(n):
    x[i] = float(input('x[' + str(i) + ']= '))
    y[i] = float(input('y[' + str(i) + ']= '))

for i in range(n):
    sxy += x[i] * y[i]
    sx += x[i]
    sy += y[i]
    sx2 += x[i] ** 2

b = ((n * sxy) - (sx * sy)) / ((n * sx2) - sx ** 2)
a = (sy - (b * sx)) / n

print("Values of a and b are %.3f and %.3f" % (a, b))

plt.scatter(x, y, color='red', label='Data Points')         # Scatter plot of original data
y_pred = a + b * x                                          # Regression line values
plt.plot(x, y_pred, color='blue', label='Best Fit Line')   # Regression line

plt.title('Linear Regression using Least Squares')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
