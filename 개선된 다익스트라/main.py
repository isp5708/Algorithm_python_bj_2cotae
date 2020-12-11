import sys
import heapq

input= sys.stdin.readline
INF=int(1e9)#무한 값저장

#노드의 개수와 간선의 개수 저장
n,m=map(int,input().split())

#시작 노드
start=int(input())

#그래프 간선들 비용 등록
graph=[[] for i in range(n+1)]

#거리 저장
distance=[INF]*(n+1)

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)

        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now]<dist:
            continue

        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost=i[1]+dist

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print('갈수없음')
    else:
        print(distance[i])

'''
시간복잡도: ElogV  v:노드 개수 e: 간선개수
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
