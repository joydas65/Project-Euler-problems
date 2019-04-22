import math

import sys

d = dict()

for b in range(3001):
    
    for a in range(1,b):
        
        c = math.sqrt((a*a)+(b*b))
        
        if c % 1 == 0:
            
            c = int(c)
            
            if (a+b+c) not in d:
                
                d[(a+b+c)] = list()
                
                d[(a+b+c)].append((a,b,c))
                
            else:
                
                d[(a+b+c)].append((a,b,c))
                
for _ in range(int(input())):
    
    n = int(input())
    
    if n not in d:
        
        print("-1")
        
    else:
        
        ans = -sys.maxsize
        
        for i in d[n]:
            
            ans = max(ans, i[0]*i[1]*i[2])
            
        print(ans)
