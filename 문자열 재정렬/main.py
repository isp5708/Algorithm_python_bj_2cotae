data=list(input())

number=['1','2','3','4','5','6','7','8','9','0'] #isalpha 사용하자

sum=0
tmp=[]
for i in range(len(data)):
    if data[i] in number:
        sum+=int(data[i])
    else:
        tmp.append(data[i])

tmp.sort()

for i in tmp:
    print(i,end='')
print(str(sum))


