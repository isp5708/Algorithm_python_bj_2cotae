dataNum=int(input())

array=[]
for i in range(dataNum):
    array.append(int(input()))

array=sorted(array,reverse=True)

print(array)
