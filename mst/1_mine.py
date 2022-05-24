# 도시 분할 계획 (백준 1647)

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

n,m=map(int,input().split()) # n은 집의 개수, m은 길의 개수
parent=[0]*(n+1)

result=0
edges=[]
cnt=1

for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b) and cnt<n-1:
        union_parent(parent,a,b)
        result+=cost
        cnt+=1

print(result)

