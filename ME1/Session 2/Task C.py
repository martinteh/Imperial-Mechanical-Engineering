import random
import math as mt
N = int(input("input N points here"))
R = range(1, N + 1)

Nsx = []
Nsy = []
for i in R:
    Nsx = Nsx + [random.random()]
    Nsy = Nsy + [random.random()]
#print(Nsx)
#print(Nsy)
NcCount = []
NsxRange = range(0, len(Nsx))
for j in NsxRange:
    if mt.sqrt(((Nsx[j]-0.5)**2)+((Nsy[j]-0.5)**2)) < 0.5:
        NcCount = NcCount + [1]
#print(NcCount)
Pi = (sum(NcCount)/N)*4
print(Pi)


#code needs cleaning up, removal of unneccessary lists to prevent too much looping