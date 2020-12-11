#잠겨있는 자물쇠 : nxn 정사각 격자
#열쇠는 mxm 정사각 격자 형태

#열쇠는 회전과 이동 가능
#자물쇠의 비어있는홈을 다채워야 자물쇠를 열수있다. 즉 홈에 맞는 열쇠 돌기를 찾아라

def rotate_a_matrix_by_90_degree(r):
    n = len(r)  # 행
    m = len(r[0])  # 열

    result = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = r[i][j]

    return result
def check(new_lock):
    lock_length=len(new_lock)//3

    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j]!=1:
                return False

    return True

def solution(key, lock):
    n=len(key)# 열쇠 길이
    m=len(lock)# 자물쇠 길이

    new_lock=[[0]*(m*3) for i in range(m*3)]

    for i in range(m):
        for j in range(m):
            new_lock[i+m][j+m]=lock[i][j]

    for i in range(4): #90도씩돌림
        key=rotate_a_matrix_by_90_degree(key) #90도 회전

        for x in range(m*2):
            for y in range(m*2):

                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j]+=key[i][j]

                if check(new_lock)==True:
                    return True

                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j]-=key[i][j]

    return False

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]])) #0은 홈부분, 1은 돌기 부분

