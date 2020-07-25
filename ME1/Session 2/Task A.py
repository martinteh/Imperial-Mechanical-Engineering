import random
#task A
'''for i in range(int(input("input N times here"))):
    print("I need to comment my scripts. Comments are marked too!")'''
 
'''R = range(1, int(input("input N times here"))+1)    
X = []
for i in R:
    X = X + [i]
#print(X)
#finding the sum of n^2 natural numbers
sqX = []
for X_value in X:
    sqX.append(X_value**2)
print(sqX)
print("The sum of the n^2 natural numbers is:", sum(sqX))'''

#N times dice throw
R = range(1, int(input("input N times here"))+1)    
X = []
for i in R:
    X = X + [int(random.random()*6 + 1)] #the print happens n times and is put into a list
print(X)
print("The sum of a dice throw N times is:", sum(X))

#factorial of a number
N = int(input("input N times here"))
factorial = 1 #every factorial is multplied by 1
for i in range(1, N+1):
    factorial = factorial*i #the original factorial is then multiplied by the index i in the range
print("The factorial is:", factorial)

