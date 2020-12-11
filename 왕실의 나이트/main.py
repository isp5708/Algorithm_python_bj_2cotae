input_data = input()

row= int(input_data[1])
column=ord(input_data[0])-96

knightRoute=[(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2),(2,1),(2,-1)] #위 왼쪽,오른쪽 오른쪽 위,아래 왼쪽 위,아래 아래 오른쪽,왼쪽

count=0
for i in knightRoute:
    nrow=row+i[0]
    ncolumn=column+i[1]

    if nrow<1 or nrow>8 or ncolumn<1 or ncolumn>8:
        continue
    count+=1

print(count)