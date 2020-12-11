import heapq
#회전판에 먹어야할 음식 N개
#1부터 n까지 번호가 붙어있다.
#각 음식을 섭취하는데 일정 시간이 소요

# 무지는 1번부터 먹기시작함. 회전판에 의해 다시 1번음식이 무지앞으로옴
#무지는 음식하나를 1초섭취후 남은음식을 그대로 두고 다음음식을 섭취함. 가장가까운번호음식
# 회전판이 다음 음식을 무지 앞으로 ㄱ가져오는데 걸ㄹ리는 시간은 없다.

#k초후에 네트워크 장애  몇번 음식부터 섭취해야하나
#섭취 음식이 없으면 -1 반환
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # 음식시간, 노드번호

    length = len(food_times)
    previous = 0
    sum_value = 0

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        previous = now
        length -= 1

    result = sorted(q, key=lambda x: x[1])
    return q[(k - sum_value) % length][1]
food_times=[3,1,2]
k=5
print(solution(food_times,k))

