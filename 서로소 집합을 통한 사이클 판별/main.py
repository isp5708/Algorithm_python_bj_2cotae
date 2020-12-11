#특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 떄까지 재귀적 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드의 개수와 간선(union 연산)의 개수 입력받기
v,e=map(int,input().split())

parent=[0]*(v+1)#부모 테이블 초기화

for i in range(1,v+1):
    parent[i]=i

cycle= False #사이클 발생 여부

for i in range(e):
    a,b= map(int,input().split())
    #사이클이 발생할경우 종료

    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    #사이클이 발생하지 않을경우 합집합 수행
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클")
else:
    print("노우")