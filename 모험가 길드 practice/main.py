n=int(input())

#공포도가 X인 모험가는 반드시 X명이상으로 구성한 모험가 그룹에 참여해야 여행가능
#최대몇개의 그룹을 만둘수있나?

fear=list(map(int,input().split()))

fear.sort()

result = 0 #총 그룹의 수
count=0 # 현재 그룹에 포함된 모험가의 수

for i in fear:
    count+=1
    if count>=i:
        result+=1
        count=0

print(result)

'''
5
2 3 1 2 2
'''
