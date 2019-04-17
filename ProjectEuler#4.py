arr = []

i,j = 100,100

while i <= 999:
    
    while j <= 999:
        
        if i*j >= 100000:
            
            s = str(i*j)
            
            if s == s[::-1]:
                
                arr.append(i*j)
        
        j += 1
        
    i += 1
    
    j = i
    
arr = sorted(arr)

#print(len(arr))

for _ in range(int(input())):
    
    n = int(input())
    
    for i,j in enumerate(arr):
        
        if j >= n:
            
            print(arr[i-1])
            
            break
