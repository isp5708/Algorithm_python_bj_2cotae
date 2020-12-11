#두 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드의 개수 와 간선(union 연산)의 개수 입력받기
v,e = map(int,input().split())
parent=[0]*(v+1) #부모테이블 초기화

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]

result=0

#부모테이블에서, 부모를 자기로 초기화
for i in range(1,v+1):
    parent[i]=i

#간선 정보 입력
for i in range(e):
    a,b,c=map(int,input().split())#노드 a에서 노드 b로 가는 비용 c
    edges.append((c,a,b)) #비용순으로 정렬하기위해 맨앞에둠

edges.sort()

#간선 하나씩 확인
for edge in edges:
    cost,a,b=edge
    #같은 집합에 속해있으면 사이클 임..
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)

'''
입력예 
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''