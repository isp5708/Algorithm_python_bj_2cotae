from collections import deque
#사과를 먹으면 뱀 길이가 늘어남.
#뱀이기어다니다 벽또는 자기자신의 몸과 부딪히면 게임 끝
#nxn 정사각 보드위에서 진행
# 몇몇칸에는 사과가 놓여져있다
# 맨위 맨 좌측 위치 뱀의 길이는 1
# 방향 오른쪽보고있음

#사과의 위치와 뱀의 이동 경로가 주어질때 이 게임이 몇초에 끝나는지 계산

n=int(input()) #보드크기
k=int(input()) #사과의 개수

data=[[0]*n for i in range(n)] #순수 맵 정보 0이동할수 있는곳 , 1사과가 있는곳 , 2 뱀의 몸통이있는곳

way=1 #맨처음 오른쪽을 보고있기 때문에
dx=[-1,0,1,0] #위 , 오른쪽, 아래 왼쪽 으로 가는데 드는 비용
dy=[0,1,0,-1]

time=0
x,y=0,0 # 뱀의 시작위치

for i in range(k):
    a,b=map(int,input().split())
    data[a-1][b-1]=1

d=deque()
L=int(input())
for i in range(L):
    a,b=map(str,input().split())
    d.append((int(a),b))

xl,c=d.popleft()
snakeMoveIndex=[(0,0)]
snakeLength=1
while True:
    if time==xl: #방향 전환
        if c=='L':
            way-=1
            if way==-1:
                way=3
        elif c=='D':
            way= (way+1)%4

        if d:
            xl,c=d.popleft()

    nx=x+dx[way]
    ny=y+dy[way]
    time+=1
    #움직인 칸에 사과가 있으면 몸통증가 , 벽이나 자기몸이면 실패 1,2

    if nx <0 or ny <0 or nx>= n or ny >=n: #벽에 부딛힐시 종료
        break

    if data[nx][ny]==1:
        snakeLength+=1
    elif data[nx][ny]==2:
        break
    x, y = nx, ny
    snakeMoveIndex.append((x,y))

    data[x][y]=2
    tmp=len(snakeMoveIndex)-snakeLength-1
    nx,ny=snakeMoveIndex[tmp]
    data[nx][ny]=0

print(time)

'''
입출력#1
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

입출력#2
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

입출력#3
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''