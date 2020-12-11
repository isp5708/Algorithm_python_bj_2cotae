from collections import deque

dx=[0,0,1,-1,-1,1,-1,1] # 위,아래, 오른쪽, 왼쪽, 왼쪽위 , 오른쪽 위, 왼쪽 아래, 오른쪽 아래
dy=[-1,1,0,0,-1,-1,1,1]

data=[]

for i in range(5):
    data.append(list(input()))

n=int(input())

def bfs():
    checkWord=[0]*len(word)

    while q:
        nowI,nowJ,wordIndex=q.popleft()

        if wordIndex==len(word)-1:
            return True

        checkWord[wordIndex] = 1
        wordIndex+=1

        for i in range(8):
            nx=dx[i]+nowI
            ny=dy[i]+nowJ

            if nx>=0 and nx<5 and ny>=0 and ny<5:
                if word[wordIndex]==data[nx][ny] :
                    q.append((nx,ny,wordIndex))

    return False





for i in range(n):
    word=input()
    startIndex=[]
    result=[]

    for i in range(5):
        for j in range(5):
            if word[0]==data[i][j]:
                startIndex.append((i,j))
    q = deque()
    for j in range(len(startIndex)):
        q.clear()
        x,y=startIndex[j]
        q.append((x,y,0))

        result.append(bfs())

    if True in result:
        print('YES')
    else:
        print('NO')

'''
URLPM
XPRET
GIAET
XTNZY
XOQRS
'''
