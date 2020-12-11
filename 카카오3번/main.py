def solution(info, query):
    language=[]
    job_group=[]
    career=[]
    soul_food=[]
    score=[]
    result=[0]*len(query)

    for i in range(len(info)):
        tmp=info[i].split()
        language.append(tmp[0])
        job_group.append(tmp[1])
        career.append(tmp[2])
        soul_food.append(tmp[3])
        score.append(tmp[4])

    for i in range(len(query)): #쿼리 갯수
        query[i]=query[i].replace(' and','')
        tmp=query[i].split()
        #tmp에 쿼리를 담아둠

        count =0


        for j in range(len(language)): #사람수만큼 검사

            check = [False] * 5

            for x in range(len(tmp)):
                if tmp[x] == '-':
                    check[x] = True

            if tmp[0]==language[j]:
                check[0]=True
            if tmp[1]==job_group[j]:
                check[1]=True
            if tmp[2]==career[j]:
                check[2]=True
            if tmp[3]==soul_food[j]:
                check[3]=True
            if int(tmp[4])<=int(score[j]):
                check[4]=True

            if False in check:
                continue
            else:
                count+=1

        result[i]=count
    return result

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
               ))