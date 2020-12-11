import sys
input=sys.stdin.readline

INF=int(1e9) #무한값

#노드 간선 개수
n,m=map(int,input().split())

#시작노드 번호 입력
start= int(input())

#거리저장
distance= [INF]*(n+1)

#방문기록
visited=[False]*(n+1)

#노드 간선 값 저장
graph=[[] for i in range(n+1)]

#간선 저장
for i in range(m):
    a,b,c=map(int,input().split())
    #간선 a에서 b로의 비용은 c
    graph[a].append((b,c))

#방문하지 않은 노드중에 가장 짧은 노드선택
def get_smallest_node():
    index=0
    min_value=INF

    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            index=i
            min_value=distance[i]

    return index

def dijkstra(start):
    visited[start]=True
    distance[start]=0

    for i in graph[start]: #시작노드와 연결된 노드들의 간선 거리를 등록
        distance[i[0]]=i[1]

    for i in range(n-1): #시작노드 제외하고 모든 노드들 체크
        now=get_smallest_node() #길이가 가장 짧은 노드를 가저옴

        visited[now]=True #방문처리

        for j in graph[now]:
            cost= j[1]+distance[now]

            if distance[j[0]]>cost: #최종비용이 더작을시 교체
                distance[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("못가는길")

    else:
        print(distance[i])

#시간복잡도는 v제곱