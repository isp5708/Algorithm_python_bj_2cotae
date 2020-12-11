def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2

    #찾을시
    if array[mid]==target:
        return mid
    #더 작은경우
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    #더큰경우
    else:
        return binary_search(array,target,mid+1,end)


n, target = map(int, input().split())
array=list(map(int,input().split()))

result= binary_search(array,target,0,n-1)

if result==None:
    print('탐색 실패')
else:
    print(result+1)