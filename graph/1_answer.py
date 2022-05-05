# 답에선 dfs로 문제 해결

n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]

def dfs(x,y):
    
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==0: #노드를 아직 방문 안했으면
        graph[x][y]=1 #방문 처리 후 dfs 진행
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
        
    


cnt=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            cnt+=1

print(cnt)