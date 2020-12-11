n=int(input())

data=list(map(int,input().split()))
operator=list(map(int,input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈

min_value=1e9
max_value=-1e9

def dfs(start,value):
    global min_value,max_value

    if start==n:
        if min_value>value:
            min_value=value

        if max_value<value:
            max_value=value

        return

    if operator[0] !=0: # 덧셈일시
        operator[0]-=1
        dfs(start+1,value+data[start])
        operator[0]+=1

    if operator[1] !=0: #뺄샘일시
        operator[1]-=1
        dfs(start+1,value-data[start])
        operator[1]+=1

    if operator[2] !=0: #곱셈
        operator[2]-=1
        dfs(start+1,value*data[start])
        operator[2]+=1

    if operator[3] !=0: #나눗셈
        operator[3]-=1
        dfs(start+1,int(value/data[start]))
        operator[3]+=1

dfs(1,data[0])

print(max_value)
print(min_value)


'''
#입력 예시 1
2
5 6
0 0 1 0

#입력 예시 2
3
3 4 5
1 0 1 0

#입력예시 3
6
1 2 3 4 5 6
2 1 1 1
'''