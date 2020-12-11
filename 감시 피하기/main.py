
n=int(input())

data=[]
t_data=[]

for i in range(n):
    data.append(list(map(str,input().split())))

    for j in range(n):
        if data[i][j]=='T':
            t_data.append((i,j))

dx=[-1,1,0,0] #상,하,좌,우
dy=[0,0,-1,1]

def find_student(x,y): #선생의 위치받아옴

    for i in range(4):
        tx, ty = x, y
        while True:
            nx=tx+dx[i]
            ny=ty+dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<n:
                if data[nx][ny]=='S':
                    return False

                if data[nx][ny]=='O':
                    break

                tx,ty=nx,ny
            else:
                break
    return True
c=False

def wall(count):
    global c

    if count==3:

        check = [False] * len(t_data)
        for i in range(len(t_data)):
            x,y=t_data[i]
            if find_student(x,y):
                check[i]=True
            else:
                check[i]=False
                break
        if False not in check:
            c=True
        return

    for i in range(n):
        for j in range(n):
            if data[i][j]=='X':
                data[i][j]='O'
                wall(count+1)
                data[i][j]='X'


wall(0)

if c==True:
    print('YES')
else:
    print('NO')

'''
#입력예시 1
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

#입력예시 2
4
S S S T
X X X X
X X X X
T T T X
'''