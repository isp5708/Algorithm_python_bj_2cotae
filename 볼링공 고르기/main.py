n,m=map(int,input().split())

data=list(map(int,input().split()))

count=0

for i in range(n):
    now=data[i]

    for j in range(i,n):
        if now!=data[j]:
            count+=1

print(count)