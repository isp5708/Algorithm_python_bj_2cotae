data=input()

count=[0]*2

now=data[0]
count[int(now)]+=1
for i in data:
    if now==i:
        continue
    else:
        now=i

        if i=='0':
            count[0]+=1
        else:
            count[1]+=1

print(min(count[0],count[1]))

