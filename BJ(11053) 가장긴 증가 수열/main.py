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
6
10 20 10 30 20 50
'''