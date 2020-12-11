def solution(s):
    #문장려에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부
    answer = len(s)

    for i in range(1,len(s)//2+1): #두개씩 압축할때 넘어버릴수도있어 +1이필요
        tmp=''
        prev=s[0:i]
        count=1
        for j in range(i,len(s),i):
            if prev==s[j:j+i]:
               count+=1
            else:
                tmp+=str(count)+prev if count >=2 else prev
                prev=s[j:j+i] #다시 상태 초기화
                count=1
        tmp+= str(count)+prev if count>=2 else prev
        answer=min(answer,len(tmp))

    return answer

solution('aabbaccc')