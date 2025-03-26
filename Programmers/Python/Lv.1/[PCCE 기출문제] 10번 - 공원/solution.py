"""
https://school.programmers.co.kr/learn/courses/30/lessons/340198

[ Implementaion ]

mats에서 작은 것부터 시행하기 위해 정렬 ··· (1)

park를 돌면서 돗자리가 깔리지 않은 공간이라면 ··· (2)

작은 돗자리부터 check_mat를 통해 깔아본다
이 때 아무 mats도 깔 수 없다면 check_mat는 -1을 return 하게 된다 ··· (3)

mats에서 mat를 가져와서 available 여부를 체크하는데 ··· (4)

index out인 경우에는 깔 수 없으므로 예외 처리한다 ··· (5)

index out이 아닌 경우에 -1인지 확인하고 모든 칸이 -1이라면 ··· (6)

return True를 한다 ··· (7)

"""


def available(mat,i,j,park):
    n = len(park)
    m = len(park[i])
    # (5)
    if i + mat > n:
        return False
    if j + mat > m:
        return False
    # (6)
    for a in range(i,i+mat):
        for b in range(j,j+mat):
            if park[a][b] != '-1':
                return False
    # (7)
    return True
    

def check_mat(mats,i,j,park):
    ret = -1
    for mat in mats:
        #print(i,j,mat,available(mat,i,j,park))
        # (4)
        if available(mat,i,j,park):
            ret = mat
        else:
            break
    return ret

def solution(mats, park):
    answer = -1
    # (1)
    mats.sort()
    for i in range(len(park)):
        for j in range(len(park[i])):
            # (2)
            if park[i][j] == '-1':
                # (3)
                answer = max(answer,check_mat(mats,i,j,park))
    return answer