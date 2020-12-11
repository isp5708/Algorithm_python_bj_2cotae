n,m =map(int,input().split())
x,y,d=map(int,input().split())

#현재 방문한곳 체크
checkMap=[[0]*m for i in range(n)]

checkMap[x][y]=1

#북 동 남 서 방향 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]

mapArray=[]
for i in range(n):
    mapArray.append(list(map(int,input().split())))

def turnLeft():
    global d
    d-=1
    if d==-1:
        d=3

count=1 #횟수
turnCount=0 #회전횟수
while True:
    #왼쪽으로 회전
    turnLeft()

    nx=x+dx[d]
    ny=y+dy[d]

    #유저가 안간곳,육지인곳만 가도록하는 조건문
    if mapArray[nx][ny]==0 and checkMap[nx][ny]==0:
        x,y=nx,ny
        checkMap[nx][ny]=1
        turnCount=0
        count+=1
        continue

    turnCount+=1

    #네곳이 전부 막혀있는곳
    if turnCount==4:
        nx= x-dx[d]
        ny= y-dy[d]

        if mapArray[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        turnCount=0


print(checkMap)
print(mapArray)
print(count)
