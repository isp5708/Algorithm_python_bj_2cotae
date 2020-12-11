#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀적 호출
    if x!=parent[x]:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[a]=b
    else:
        parent[b]=a

#노드의 개수와 간선(union 연산)의 개수 입력
v,e=map(int,input().split())
parent=[0]*(v+1) #부모테이블 초기화

#부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

#union 연산으 각각 수행
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

print ('각 원소가 속한 집합: ',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()
#부모테이블 내용출력
print('부모 테이블: ',end='')
for i in range(1,v+1):
    print(parent[i],end=' ')