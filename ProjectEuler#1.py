for _ in range(int(input())):
    
    n = int(input())
    
    if n%3 == 0:
        
        three = (n//3)-1
        
    else:
        
        three = n//3
        
    if n%5 == 0:
        
        five = (n//5)-1
        
    else:
        
        five = n//5
        
    if n%15 == 0:
        
        fifteen = (n//15)-1
        
    else:
        
        fifteen = (n//15)
        
    ans = 3*(three*(three+1))//2
    
    ans += 5*(five*(five+1))//2
    
    ans -= 15*(fifteen*(fifteen+1))//2
    
    print(ans)
