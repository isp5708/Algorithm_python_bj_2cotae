n = int(input())

cnt = 0

for i in range(n+1):
    for j in range(60):
        for t in range(60):
            if '3' in str(i)+str(j)+str(t):
                cnt+=1

print(cnt)
