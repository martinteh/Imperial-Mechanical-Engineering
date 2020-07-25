#task D
import math as mt
import matplotlib.pyplot as plt

N = 100
R = range(1, N+1, 5)
x = []
for i in R:
    x = x + [i]
print(x)
    
y = []
for x_value in x:
    y = y + [mt.log(x_value, 10)]
print(y)

plt.scatter(x, y)
