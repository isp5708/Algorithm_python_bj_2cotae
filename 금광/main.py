

for i in range(int(input())):
    n,m=map(int,input().split())
    data=list(map(int,input().split()))

    #데이터 추가
    dp=[]
    index= 0
    for i in range(n):
        dp.append(data[index:index+m])
        index+=m

    for i in range(1,m):
        for j in range(n):
            #왼쪽위
            if j==0:
                left_up=0
            else:
                left_up=dp[j-1][i-1]

            #왼쪽아래
            if j==n-1:
                left_down=0
            else:
                left_down=dp[j+1][i-1]

            left_left=dp[j][i-1]

            dp[j][i]= dp[j][i]+max(left_up,left_left,left_down)

    result=0
    for i in range(n):
        result=max(result,dp[i][m-1])

    print(result)
