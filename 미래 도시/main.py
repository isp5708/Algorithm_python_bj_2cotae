n,m=map(int,input().split())

INF=int(1e9)
graph=[[INF]*(n+1) for i in range(n+1)]

for i in range (1,n+1):
    graph[i][i]=0

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k=map(int,input().split()) # 소개팅상대 k , x번 회사    k먼저갔가 k번에서 x로감


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

distance=graph[1][k]+graph[k][x]

if distance>=INF:
    print("-1")
else:
    print(distance)

'''
출력예시 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
출력예시 2
4 2
1 3
2 4
3 4
'''