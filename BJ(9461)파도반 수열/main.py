t= int(input())

data=[0]*t

for i in range(t):
    data[i]=int(input())

dp=[0]*(max(data)+1)

if max(data)<4:
    print(1)
    exit()

dp[1]=1
dp[2]=1
dp[3]=1

for i in range(4,len(dp)):
    dp[i]=dp[i-2]+dp[i-3]

for i in range(len(data)):
    print(dp[data[i]])
