# 팀 결성

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


n,m=map(int,input().split()) # 0~n번까지의 번호 부여, m은 union의 개수
parent=[0]*(n+1)

for i in range(n+1):
    parent[i]=i

for i in range(m):
    x,a,b=map(int,input().split())
    if x==0: # union 연산
        union_parent(parent,a,b)
    else: # find 연산
        if find_parent(parent,a)==find_parent(parent,b):
            print("YES")
        else:
            print("NO")
        