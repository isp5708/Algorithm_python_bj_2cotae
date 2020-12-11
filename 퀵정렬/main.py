array= [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>= end:
        return

    pivot= start
    left= start+1
    right= end

    #왼쪽이 작음 오른쪽이 큼
    while left<=right:
        while array[left]<=array[pivot] and left<=end:
            left+=1

        while array[right]>=array[pivot] and right>start: #start는 피벗이기때문에 =을빼줌
            right+=1

        #교차시
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        #교차아닐시 왼쪽과 오른쪽 교환
        else:
            array[left],array[right]=array[right],array[left]

    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(quick_sort)