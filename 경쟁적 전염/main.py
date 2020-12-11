from collections import deque

n,k=map(int,input().split()) # n x n 시험관 1번 ~ k번까지 바이러스

data=[]
dx=[-1,1,0,0] #상, 하, 좌, 우
dy=[0,0,-1,1]
virus=[]

for i in range(n):
    data.append(list(map(int,input().split())))
    for j in range(n):
        #해당 위치에 바이러스가 존재하는 경우
        if data[i][j]!=0:
            virus.append((data[i][j],0,i,j)) # 바이러스번호, 시간, x,y좌표

virus.sort()
q=deque(virus)

s,x,y=map(int,input().split()) #s초 x,y에 존재하는 바이러스 종류는?

while q:
    c,d,a,b = q.popleft()

    if d==s:
        break

    for i in range(4):
        nx= dx[i]+a
        ny= dy[i]+b

        if nx>=0 and nx< n and ny>=0 and ny<n:
            if data[nx][ny]==0:
                data[nx][ny]=c
                q.append((c,d+1,nx,ny))


print(data[x-1][y-1])

'''
#입력예시 1
3 3
1 0 2
0 0 0
3 0 0
2 3 2

#입력예시 2
3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''