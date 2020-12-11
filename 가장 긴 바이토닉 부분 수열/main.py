
n= int(input())

data=list(map(int,input().split()))

dpFront=[1]*n
dpBack=[1]*n

for i in range (1,n):
    m=0

    for j in range(i):
        if data[i]>data[j]:
            if m<dpFront[j]:
                m=dpFront[j]

    dpFront[i]=m+1

for i in range (n-2,-1,-1):
    m=0

    for j in range(n-1,i,-1):
        if data[i]>data[j]:
            if m<dpBack[j]:
                m=dpBack[j]

    dpBack[i]=m+1

for i in range(n):
    dpBack[i]=dpFront[i]+dpBack[i]-1

print(max(dpBack))


'''
10
1 5 2 1 4 3 4 5 2 1
'''