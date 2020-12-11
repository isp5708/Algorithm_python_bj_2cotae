import sys
import copy
from collections import deque

n,m=map(int,sys.stdin.readline().split())

data=[]

for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

dx=[1,0,-1,0]#아래, 오른쪽, 위, 왼쪽
dy=[0,1,0,-1]

result=0

def bfs():
    global result
    tmp=copy.deepcopy(data)

    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                q.append([i,j])

    while q:
        nowX,nowY=q.popleft()

        for i in range(4):
            nx=nowX+dx[i]
            ny=nowY+dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<m:
                if tmp[nx][ny]==0:
                    tmp[nx][ny]=2
                    q.append([nx,ny])

    cnt=0
    for i in tmp:
        cnt+=i.count(0)
    result=max(result,cnt)

def wall(x):
    if x==3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                wall(x+1)
                data[i][j]=0

q=deque()
wall(0)
print(result)

'''
n,m= map(int,input().split())

data=[]
temp=[[0]*m for i in range(n)]

for i in range(n):
    data.append(list(map(int,input().split())))

dx=[1,0,-1,0] # 아래, 오른쪽, 위, 왼쪽
dy=[0,1,0,-1]

result=0

def virus(x,y):

    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

def getScore():
    s=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                s+=1

    return s

def dfs(count):
    global result

    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)

        result=max(result,getScore())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1

dfs(0)
print(result)'''


'''
#입력 예시1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

#입력 예시 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

#입력 예시3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

'''