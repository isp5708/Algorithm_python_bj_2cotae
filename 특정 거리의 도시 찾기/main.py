from collections import deque

n,m,k,x = map(int,input().split()) #도시의개수 N, 도로의 개수 M, 거리정보 K, 출발 도시의 번호 X

graph=[[] for _ in range(n+1)] #맨 앞 비워둠 보통

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

distance = [-1]*(n+1)

distance[x]=0

q= deque([x])

while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node]==-1:
            distance[next_node]=distance[now]+1
            q.append(next_node)

check=False

for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True

if check==False:
    print(-1)