for _ in range(int(input())):
    
    n = int(input())
    
    x = (n*(n+1)*((2*n)+1))//6
    
    y = (n*(n+1))//2
    
    y = y*y
    
    print(y-x)
