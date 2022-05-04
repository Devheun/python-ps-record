# 음료수 얼려먹기
from collections import deque

def bfs(x,y):
    
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    
    while queue:
        v1,v2=queue.popleft()
        visited[v1][v2]=True
        
        for i in range(4):
            nx=v1+dx[i]
            ny=v2+dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny<=M:
                continue
            elif visited[nx][ny]==True or array[nx][ny]==1:
                continue
            queue.append((nx,ny))
            
    return True
                
            
    
    
    
    

N,M=map(int,input().split())
array=[list(map(int,input())) for _ in range(N)] #띄어쓰기 없을 때 구분해서 입력받는 방법

visited=[[False]*M for _ in range(N)]
queue=deque([])
cnt=0

dx=[0,0,1,-1] #동서남북
dy=[1,-1,0,0]

for i in range(N):
    for j in range(M):
        if array[i][j]==0 and visited[i][j]==False:
            if bfs(i,j)==True:
                cnt+=1

print(cnt)

