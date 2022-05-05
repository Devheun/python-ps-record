# 미로 탈출(dfs 이용)

def dfs(x,y,cnt): #좌표와 몇번 이동했는지 칸수
    
    if x==n-1 and y==m-1:
        print(cnt)
        exit()
    
    graph[x][y]=0
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==1:
            dfs(nx,ny,cnt+1)
    
    
    


n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)] # 여기선 출발위치 (0,0), 출구 (n-1,m-1)로 가정

dx=[-1,1,0,0] # 상하좌우
dy=[0,0,-1,1]

dfs(0,0,1)

