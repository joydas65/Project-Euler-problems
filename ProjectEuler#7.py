prime = [True for i in range(200001)]

p = 2

while p*p <= 2*(10**5):
    
    if prime[p] == True:
        
        for i in range(p*p, 200001, p):
            
            prime[i] = False
            
    p += 1
    
primes = []
    
for p in range(2,200001):
    
    if prime[p]:
        
        primes.append(p)
        
for _ in range(int(input())):
    
    print(primes[int(input())-1])
