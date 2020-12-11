inputNum=int(input())

array=[]

for i in range(inputNum):
    data=input().split()
    array.append([data[0],int(data[1])])

array=sorted(array,key=lambda student: student[1],reverse=True)

for student in array:
    print(student[0],end=' ')