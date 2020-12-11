import math, copy
from collections import deque


def prime_check(n):  # n값이 소수인지 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def bfs(A, B):
    answer = 0
    # 한자리 값을 다루기 위해서 int -> string 변환

    q = deque([[list(str(A)), 0]])
    visited = {A}

    while True:
        val, cnt = q.popleft()
        if int("".join(map(str,val))) == B:
            return cnt
        else:
            for i in range(4):  # 각자리 변환
                for j in range(10):  # 변환 값
                    if val[i] == str(j):
                        continue
                    else:
                        temp = copy.deepcopy(val)
                        temp[i] = str(j)  # 값 변환
                        temp_value = int("".join(map(str, temp)))
                        if temp_value not in visited and temp_value >= 1000 and prime_check(temp_value):  # 조건 확인
                            visited.add(temp_value)
                            q.append([temp, cnt + 1])


if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(bfs(A, B))

'''
import math
from collections import deque
start,end= map(str,input().split())
index=0

d=[False]*10001
prime=[]
for i in range(1001,10000):

    cnt=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            cnt+=1

    if cnt==0:
        d[i]=True
        prime.append(str(i))
        if start==str(i):
            index=len(prime)-1

graph=[[] for i in range(len(prime))]

for i in range(len(prime)):
    a=str(prime[i])
    for j in range(len(prime)):
        if i==j:
            continue

        b=str(prime[j])

        cnt=0

        for t in range(4):
            if a[t]==b[t]:
                cnt+=1

        if cnt==3:
            graph[i].append([b,j]) # 값과 노드번호 추가

q=deque() #인덱스와 횟수
q.append([start,index,0])

def bfs():

    while q:
        now,nowIndex,cnt=q.popleft() # 현재값, 인덱스, 카운트

        if now==end:
            return cnt

        for i in range(len(graph[nowIndex])):
            b,j=graph[nowIndex][i] #값과 노드번호
            q.append([b,j,cnt+1])

print(bfs())'''

