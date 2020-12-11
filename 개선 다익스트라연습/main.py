import sys
import heapq
input=sys.stdin.readline

INF=int(1e9)

#노드의 개수, 간선의 개수
n,m=map(int,input().split())
start=int(input())

graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))  #노드 a에서 노드 b로 c만큼의 비용

def dijkstra(start):
    q=[]
    #시작노드의 비용, 노드번호 큐에삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #가장 짧은 거리 노드 꺼내기
        dist,now=heapq.heappop(q)

        if distance[now]>dist:
            continue

        for i in graph[now]:
            cost= i[1]+dist
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print('갈수가업저영')
    else:
        print(distance[i])