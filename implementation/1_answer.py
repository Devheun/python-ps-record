# 상하좌우 문제

n=int(input())
x,y=1,1
plans=input().split()

# 움직임의 종류를 미리 리스트에 담아 둠. L R U D 순서대로
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
        
    if nx<1 or nx>n or ny<1 or ny>n:continue
        
    x=nx
    y=ny

print(x,y)