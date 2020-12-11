n=int(input())

data=[]

dp=[1]*n

for i in range(n):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x:x[0])


for i in range(n):
    m=0

    for j in range(i):
        if data[i][1]>data[j][1]:
            if dp[j]>m:
                m=dp[j]

    dp[i]=m+1

print(n-max(dp))


'''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
'''