
def dfs(graph,v,visited):
    visited[v]=True #방문 처리
    print(v,end=' ')
    for v in graph[v]:
        if not visited[v]:
            dfs(graph,v,visited)
            

# 1번노드가 2,3,8번 노드랑 연결됨
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 방문 체크용 리스트
visited=[False]*9

dfs(graph,1,visited)