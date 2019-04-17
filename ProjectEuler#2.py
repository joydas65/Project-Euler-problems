arr = [1,2]

for i in range(2,100):
    
    arr.append(arr[i-1]+arr[i-2])
    
for _ in range(int(input())):
    
    ans = 0
    
    n = int(input())
    
    for i in arr:
        
        if i % 2 == 0 and i < n:
            
            ans += i
            
        elif i >= n:
            
            break
            
    print(ans)
