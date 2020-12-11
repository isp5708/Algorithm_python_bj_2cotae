import heapq
n,m,start=map(int,input().split()) #도시의 개수 n, 통로의 개수 m, 메시지 보내고자하는 도시 c

graph=[[]for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())

    graph[a].append((b,c)) #a에서 b로가는 값이 c

INF=1e9

distance=[INF]*(n+1)

def dijkstra(start):
    q=[]

    heapq.heappush(q,(0,start)) #(값, 노드)
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist: #방문표시
            continue

        for i in graph[now]:
            cost=dist+i[1]

            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count=0
m_distance=-1
for i in range(1,n+1):
    if distance[i]!=INF:
        count+=1
        m_distance=max(m_distance,distance[i])

print(distance)
print(count-1,m_distance)