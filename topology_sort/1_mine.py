# 커리큘럼 (리스트 값 복제해야할 땐 deepcopy() 사용 !!)

from collections import deque
import copy

n=int(input())
indegree=[0]*(n+1)
graph=[[] for i in range(n+1)]

time=[0]*(n+1) #각 강의 시간

for i in range(1,n+1):
    temp=list(map(int,input().split()))
    time[i]=temp[0]
    for j in temp[1:-1]:
        indegree[i]+=1
        graph[j].append(i)
        

        
def topology_sort():
    
    result=copy.deepcopy(time)
    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        
        now=q.popleft()
        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                
    for i in range(1,n+1):
        print(result[i])
        
        

        
topology_sort()
    