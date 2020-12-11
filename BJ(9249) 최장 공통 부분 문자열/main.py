str1 = input()
str2 = input()

n=len(str1)+1
m=len(str2)+1

dp=[[0]*m for i in range(n)] # n이 row  m이 column

ans=0
idxC=0

for i in range(1,n):
    for j in range(1,m):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1

        if ans<dp[i][j]:
            ans=dp[i][j]
            idxC=j

print(ans)

for i in range(idxC-ans,idxC):
    print(str2[i],end="")


