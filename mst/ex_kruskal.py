def find_parent(parent,x):
    if x!=parent[x]:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]


def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 노드의 개수와 간선의 개수(union 연산) 입력 받기
v,e=map(int,input().split())
parent=[0]*(v+1)

edges=[] #모든 간선을 담을 리스트
result=0 # 결과값

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b)) # 비용순으로 정렬 위해 튜플 첫번째 원소 cost로

edges.sort()

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b): # 사이클을 발생시키지 않을 때만 union
        union_parent(parent,a,b)
        result+=cost

print(result)
        