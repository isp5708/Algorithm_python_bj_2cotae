n=int(input()) #포도주 개수

data=[0]

for i in range(n):
    data.append(int(input()))

if len(data)<3:
    print(sum(data))
    exit()

dp=[0]
dp.append(data[1])
dp.append(data[1]+data[2])

for i in range(3,n+1):
    dp.append(max(dp[i-2]+data[i],dp[i-1],data[i]+data[i-1]+dp[i-3]))

print(dp[n])