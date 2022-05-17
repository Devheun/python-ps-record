# 미래 도시

INF=int(1e9)
n,m=map(int,input().split()) # 전체 회사 개수 n, 경로의 개수 m
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b],graph[b][a]=1,1 # a회사에서 b회사, b회사에서 a회사가 연결된 것

x,k=map(int,input().split())

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])


if graph[1][k]>=INF or graph[k][x]>=INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])
