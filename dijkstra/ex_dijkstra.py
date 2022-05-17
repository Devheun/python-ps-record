import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

#노드, 간선 개수
n,m=map(int,input().split())

#시작 노드
start=int(input())

#각 노드에 연결된 노드 정보 담는 리스트 생성
graph=[[] for i in range(n+1)]

distance=[INF] * (n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    #a 노드에서 b 노드로 가는 비용이 c
    graph[a].append((b,c))
    
def dijkstra(start):
    q=[]
    #시작노드 -> 시작노드는 최단거리 0으로 하고 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q) # 가장 최단 거리가 짧은 노드 꺼내기
        if distance[now]<dist: # 현재 노드가 이미 처리된 적 있으면 무시
            continue
            
        for i in graph[now]: # 현재 노드와 연결된 다른 노드들을 확인
            cost=dist+i[1]
            
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    
    
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])