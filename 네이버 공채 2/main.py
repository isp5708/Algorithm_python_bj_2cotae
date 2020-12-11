def dfs(n,graph,visited,seq):

    visited[n]=True
    seq.append(n)
    for i in graph[n]:#노드가 작은것부터들어감
        if visited[i]==0:
            dfs(i,graph,visited,seq)


def solution(n,edges):
    graph=[[] for i in range(n)]
    graph_value=[0]*n
    for i in edges:
        a,b=i
        graph[a].append(b)
        graph[b].append(a)

    visited=[False]*n
    seq=[]
    for i in range(n):
        if len(graph[i])==1:
            graph_value[i]=1

            if n - 1 == i:
                dfs(i, graph, visited, seq)
                graph_value[i] = 0



    for i in range(n-1,-1,-1):
        #print(seq[i] ,end=' ') # 순회 순서
        if graph_value[seq[i]]==0:  #그래프의 값이 0일때만진행
            tmp=1 #자기자신 노드
            for j in graph[seq[i]]: #연결된 노드들을 다더함
                tmp+=graph_value[j]
            graph_value[seq[i]]=tmp
    standard=n//3

    tmp=[]
    for i in range(n):
        if graph_value[i]%standard==0:
            for j in graph[i]:
                if graph_value[j]>graph_value[i]:
                    tmp.append((i,j))
    print()
    print(tmp)
    result=[]

    for i in range(n-1):
        a,b= edges[i][0],edges[i][1]
        if (a,b) in tmp:
            result.append(i)
        if (b,a) in tmp:
            result.append(i)

    print(graph_value)
    print(sorted(result))
    print()
    return result.sort()


solution(9,[[0,2],[2,1],[2,4],[3,5],[5,4],[5,7],[7,6],[6,8]])