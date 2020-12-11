n=int(input())

data=list(map(int,input().split()))

data.reverse()

dp=[1]*n

for i in range(1,n):
    for j in range(0,i):
        if data[i]>data[j]:
            dp[i]=max(dp[j]+1,dp[i])

print(n-max(dp))

'''
7
15 11 4 8 5 2 4
'''

'''
n=int(input())

data=list(map(int,input().split()))

dp=[0]*(n+1)
dp[1]=1

for i in range (2,n+1):
    m = 0

    for j in range(1,i):
        if data[i-1]>data[j-1]:
            if m<dp[j]:
                m=dp[j]

    dp[i]=m+1

print(max(dp))
'''