import sys

for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    num = input()
    
    digits = len(num)
    
    subs = []
    
    i = 0
    
    while i+k <= digits:
        
        subs.append(num[i:i+k])
        
        i += 1
        
    ans = -sys.maxsize
        
    for i in subs:
        
        prod = 1
        
        for j in i:
            
            prod = prod * int(j)
            
        ans = max(ans, prod)
        
    print(ans)
