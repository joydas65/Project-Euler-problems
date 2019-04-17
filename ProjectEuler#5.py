def computeHCF(a,b):
    
    if a%b == 0:
        
        return b
    
    else:
        
        return computeHCF(b,a%b)

for _ in range(int(input())):
    
    n = int(input())
    
    if n <= 2:
        
        print(n)
        
    else:
        
        val = 2
        
        for i in range(3,n+1):
            
            val = (val*i)//computeHCF(max(val,i),min(val,i))
            
        print(val)
