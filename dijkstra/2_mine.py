# 전보

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)
cnt=0

n,m,c=map(int,input().split()) # n은 도시의 개수, m은 통로의 개수, c는 시작도시

#각 노드에 연결된 노드 정보 담는 리스트 생성
graph=[[] for i in range(n+1)]

distance=[INF] * (n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z)) # X 도시 -> Y 도시까지 메시지 전달시간 Z
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist: # 이미 처리된 것
            continue
            
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
            
dijkstra(c)

total_cost=0

for i in range(1,n+1):
    if distance[i]!=INF:
        cnt+=1
        total_cost=max(total_cost,distance[i])


print(cnt-1,total_cost)