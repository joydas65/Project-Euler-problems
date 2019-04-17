def computePrimeFactors(n):
    
    res = []
    
    i = 2
    
    while i*i <= n:
        
        while n%i == 0:
            
            res.append(i)
            
            n //= i
            
        i += 1
        
    if n != 1:
        
        res.append(n)
        
    return res

for _ in range(int(input())):
    
    n = int(input())
    
    print(max(computePrimeFactors(n)))
