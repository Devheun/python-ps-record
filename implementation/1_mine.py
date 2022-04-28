# 상하좌우 문제

n=int(input())

direction=input().split()
tourist=[1,1]

for i in direction:
    if i=='L':
        if tourist[1]==1:continue
        else: tourist[1]-=1
    
    elif i=='R':
        if tourist[1]==n:continue
        else: tourist[1]+=1
        
    
    elif i=='U':
        if tourist[0]==1:continue
        else: tourist[0]-=1
    
    else:
        if tourist[0]==n:continue
        else: tourist[0]+=1

print(tourist[0],tourist[1])
    
        
    