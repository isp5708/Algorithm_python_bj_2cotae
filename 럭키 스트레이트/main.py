#캐릭터의 점수를 N   자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황

n=input()
# 123402
mid=len(n)//2

left=0
right=0
for i in range(mid):
    left+=int(n[i])

for i in range(mid,len(n)):
    right+=int(n[i])

if left==right:
    print('LUCKY')
else:
    print('READY')