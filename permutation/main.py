def perm (input,i):
    if i==len(input)-1:
        print(input)

    for j in range(i,len(input)):
        input[i],input[j]=input[j],input[i]
        perm(input,i+1)
        input[i],input[j]=input[j],input[i]

perm([1,2,3],0)

n=[1,2,3]
r=2

result=[0]*r

def dfs(L,B):
    if L==r:
        print(result)
    else:
        for i in range(B,len(n)):
            result[L]=n[i]
            dfs(L+1,i+1)

dfs(0,0)