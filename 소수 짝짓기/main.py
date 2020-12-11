data = list(input())

alpa=[0]*91  #a,b,c, ~ z

alpa[ord(data[-1])]+=1

tmp=[]

index=0
for i in range(len(data)-2,-1,-1):
    index=i
    alpa[ord(data[i])]+=1
    if ord(data[i+1])> ord(data[i]):
        for j in range(65,len(alpa)):  #0이아니고 현재 값이 아닌것 알파벳들을 tmp에 추가
            if alpa[j]!=0 and j!=ord(data[i]):
                data[i]=chr(j)
                alpa[j]-=1
                break
        break
index+=1

for i in range(65,len(alpa)):
    x=alpa[i]
    if x==0:
        continue

    for j in range(x):
        data[index]=chr(i)
        index+=1

print("".join(data))

