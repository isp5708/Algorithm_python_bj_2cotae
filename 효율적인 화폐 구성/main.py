n,m = map(int,input().split())
#n은 화폐의 갯수 합이 M원

array=[]
for i in range(n):
    array.append(int(input()))

dp=[10001]*(m+1)
dp[0]=0

for i in range(n):
    for j in range(array[i],m+1):
        dp[j]=min(dp[j],dp[j-array[i]]+1)

if dp[m]==10001:
    print(-1)
else:
    print(dp[m])