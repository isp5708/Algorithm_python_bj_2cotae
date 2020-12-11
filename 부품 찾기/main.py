n= int(input())
#물건 리스트
array=list(map(int,input().split()))

m=int(input())

x=list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')