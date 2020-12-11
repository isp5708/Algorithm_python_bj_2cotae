from itertools import combinations

def solution(orders, course):
    #orders 손님 주문
    #course 조합갯수
    menu=[[0]*26 for _ in range(len(orders))]
    allMenu=[0]*26
    result=[]

    idx=0
    for i in orders:
        for j in range(len(i)):
            menu[idx][ord(i[j])-65]+=1
            allMenu[ord(i[j])-65]+=1
        idx+=1
    c=[]
    for i in range(len(allMenu)):
        if allMenu[i] !=0:
            c.append(chr(i+65))

    for i in course:
        t=list(combinations(c,i))

        cntC=[0]*len(t)
        idx=0
        for j in t: #j에 콤비네이션 담음

            count=0
            for y in orders: #orders에서 하나씩 찾음
                check=[False]* len(j)

                for x in range(len(j)): #orders에 있는 것들을 True로바꿔줌
                    if y.find(j[x])!=-1:
                        check[x]=True

                if False not in check:
                    count+=1
            cntC[idx]+=count

            idx+=1

        mx=max(cntC)

        for j in range(len(cntC)): #인덱스 번호 t에 값저장
            re = ""
            if cntC[j]==mx:
                for x in range(len(t[j])):
                    re+=t[j][x]
                result.append(re)

            #tmp 값: A,B 담김 이제 검사

    result=sorted(result)
    return result

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))