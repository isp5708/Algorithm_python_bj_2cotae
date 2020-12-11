import copy
n=int(input())

data=[[0]*n for i in range(n)]

for i in range(n):
    data[i]=list(map(int,input().split()))

dp=copy.deepcopy(data)

for i in range(1,n):
    for j in range(len(data[i])):
        if j==0:
            dp[i][j]=data[i][j]+dp[i-1][j]
        elif j==len(data[i])-1:
            dp[i][j]=data[i][j]+dp[i-1][j-1]
        else:
            dp[i][j]=data[i][j]+max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[n-1]))

'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''