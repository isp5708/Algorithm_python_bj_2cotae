n, m, k = map(int, input().split()) # 배열크기, 전체 계산 횟수, 제일큰것 반복횟수

data = list( map(int, input().split())) #리스트로 감싸줌

data.sort()

first = data[n-1]
second = data[n-2]

# 수열 (k+1) 이 반복
count= int(m/(k+1))*k
count+= m%(k+1)

result=0
result+=count*first
result+=(m-count)*second

print(result)
