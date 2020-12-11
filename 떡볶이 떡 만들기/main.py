n,m=map(int,input().split())
#떡의 개수 N, 요청한 떡의 길이 M

riceCake=list(map(int,input().split()))
#떡의 길이저장
#시작점 0 떡의 제일 큰길이  mid값
start=0
end=max(riceCake)

result=0
while start<=end:
    mid=(start+end)//2
    sum=0
    for i in riceCake: # 떡이길이가 짧으면 - 가되므로 if문으로 조건
        if i>mid:
            sum+=i-mid
    # sum 손님이 가저가는 떡
    # 적어도 m만큼의 떡을 얻기위함
    if sum<m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1


print(result)



