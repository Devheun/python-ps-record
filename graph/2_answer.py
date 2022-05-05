# 미로탈출 (bfs이용 효과적 -> 출발지점에서 가까운 노드부터 탐색)
from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1: #해당 노드를 처음 방문하는 경우에만 최단 거리 기록 (1이면 처음 방문)
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
                

print(bfs(0,0))