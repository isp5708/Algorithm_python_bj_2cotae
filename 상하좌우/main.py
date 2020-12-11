n= int(input())

data=input().split()

move_type=['R','L','U','D']
dx=[1,-1,0,0]
dy=[0,0,-1,1]

x,y=1,1



for plan in data:
    for i in range(len(move_type)):
        if plan==move_type[i]:
            nx=x+dx[i]
            ny=y+dy[i]

    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x=nx
    y=ny

print(y,x)