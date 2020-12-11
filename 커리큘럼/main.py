from collections import deque
import copy
n=int(input())

indegree=[0]*(n+1)
time=[0]*(n+1)
graph=[[] for i in range(n+1)]

for i in range(1,n+1):
    data=list(map(int,input().split()))

    time[i]=data[0]
    for x in data[1:-1]:
        indegree[i]+=1
        graph[x].append(i) # x 이수해야하는과목

def topology_sort():
    q=deque()
    result=copy.deepcopy(time)

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            q.append(i)
            indegree[i]-=1
            result[i]=time[i]+result[now]
            if indegree[i]==0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])



topology_sort()

'''
입력예시
5
10 -1
10 1 -1
4 1 -1
4 3 -1
3 3 -1
'''