from _collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#이동방향 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#0 괴물 1 이동가능
def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            # 공간 벗어날시 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            #벽일시 무시
            if graph[nx][ny]==0:
                continue
            #처음 방문시 기록
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))