from collections import deque

v,e=map(int,input().split()) # 노드, 간선 개수 입력

indegree=[0]*(v+1) #진입차수 리스트

graph=[[] for i in range(v+1)] # 각 노드에 연결된 간선 정보 담는 리스트

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b) # a 노드에서 b노드로 이동 가능
    indegree[b]+=1 # 진입차수 증가

def topology_sort():
    result=[] # 수행 결과를 담는 리스트
    q=deque()
    
    # 처음에 시작할 때 진입차수가 0인 노드 큐에 삽입
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now=q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i,end=' ')

topology_sort()
