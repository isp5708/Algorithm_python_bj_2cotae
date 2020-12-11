t= int(input())

array=[]

for i in range(t):
    array.append(int(input()))

n=max(array)

dp0=[0]*(n+1)
dp1=[0]*(n+1)

dp0[0],dp1[0]=1,0
dp0[1],dp1[1]=0,1

for i in range(2,n+1):
    dp0[i],dp1[i]=dp0[i-2]+dp0[i-1],dp1[i-2]+dp1[i-1]

for i in range(t):
    print(str(dp0[array[i]])+' '+str(dp1[array[i]]))
