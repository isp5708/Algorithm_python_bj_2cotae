n, m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    #현재 줄 가장작은 수찾기
    min_value= min(data)
    result = max(result, min_value)

print(result)