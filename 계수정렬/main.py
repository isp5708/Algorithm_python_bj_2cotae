array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

data=[0]*(max(array)+1)

for i in array :
    data[i]+=1

for i in range(len(data)):

    for j in range(data[i]):
        print(i,end=' ')


array=[('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[0]

result = sorted(array,key=setting)
print(result)