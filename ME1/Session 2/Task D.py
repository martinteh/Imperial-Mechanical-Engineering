#task D Prime Numbers up to N
N = int(input("What number do you want the primes to go up to?"))
R = range(2, N+1)

'''List = []
for i in R:
    List = List + [i]
#print(List)'''

Primes = []
for i in R:
    prime = True #assume all are primes until loop
    
    for k in range(2, i): #pick out which numbers aren't primes from this loop
        if (i % k) == 0:
            prime = False
    if prime: #use if condition, if it's a prime then add it
        Primes = Primes + [i]
            
print(Primes)
