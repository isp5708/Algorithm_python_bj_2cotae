import sys
import heapq
input=sys.stdin.readline

INF=int(1e9)

n,m,c=map(int,input().split()) #도시의 개수n (노드), 통로의개수 m(간선), 메시지 보내는 도시(출발노드) c

graph=[[] for i in range(n+1)] #노드의 정보 담는 그래프
distance=[INF]*(n+1) #거리비용을 담는 리스트

for i in range (m): #간선의 개수만큼 입력받기
    x,y,z=map(int,input().split()) # x노드에서 y노드로 가는 비용은 z
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start)) #간선의 비용, 노드

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist: #기존에 갔었던 곳이면 무시
            continue

        for i in graph[now]:
            cost=i[1]+distance[now]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0])) #간선의 비용 노드
dijkstra(c)
countryCnt=0
distance[0]=-1
sendTime=max(distance)
for i in range(1,n+1):
    if distance[i]!=INF and distance[i]!=0:
        countryCnt+=1

print(str(countryCnt)+" "+str(sendTime))

'''
3 2 1
1 2 4
1 3 2
'''