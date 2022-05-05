# 음료수 얼려먹기
from collections import deque

def bfs(x,y):
    
    queue=deque()
    queue.append((x,y)) # 방문한 위치 큐에 넣기
    visited[x][y]=True
    
    while queue:
        v1,v2=queue.popleft()
        visited[v1][v2]=True
        
        for i in range(4):
            nx=v1+dx[i]
            ny=v2+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M and array[nx][ny]==0 and visited[nx][ny]==False:
                queue.append((nx,ny))
                
                
            
    
    
    
    

N,M=map(int,input().split())
array=[list(map(int,input())) for _ in range(N)] #띄어쓰기 없을 때 구분해서 입력받는 방법

visited=[[False]*M for _ in range(N)]
cnt=0

dx=[0,0,1,-1] #동서남북
dy=[1,-1,0,0]

for i in range(N):
    for j in range(M):
        if array[i][j]==0 and visited[i][j]==False: # 구멍이 뚫려있고 방문 안했을 때
            bfs(i,j)
            cnt+=1
            

print(cnt)