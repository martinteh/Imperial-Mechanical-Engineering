import numpy as np
#task A
'''A = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
B = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

B[5] = A[2] + A[3]
print(B)

Product = B[4] * 2
print(Product)

X = A[len(A) - 1]
print(X)

Y = A[0]

A[0] = X
A[len(A)-1] = Y
print(A)

i = 3
j = 5

J = A[j]
A[j] = B[i]
B[i] = J
print(A)
print(B)'''

#task B
R = range(1, 101)
A = []
for i in R:
    A = A + [i]
print(A)

B = []
for A_value in A:
   B = B + [A_value**2]
print(B)

#without zip
#C = [A[i]+B[i] for i in range(len(A))]
#print(C)
C = []
for i in range(0, len(A)):
    C = C + [A[i]+B[i]]
print(C)
#zip function
#for (a,b) in zip(A, B):
     #print(a, b)
     
'''C=[sum(i) for i in zip(A,B)]
#print(C)

#numpy function
#C = np.add(A, B)
#print(C)


for i in range(len(A)):
    if i%3 == 0:
        A[i] = 0
print(A)

print(A[::-1]) # option 1
print(list(reversed(A))) # option 2
A.reverse() # option 3
print(A)'''