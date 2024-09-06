"""
https://school.programmers.co.kr/learn/courses/30/lessons/120924

[ Mathematics ]

등차수열인 경우엔 공차가 일정 ··· (1)

등차수열이 아니면 등비수열이다 ··· (2)
"""



def solution(common):
    # (1)
    if common[1]-common[0] == common[2]-common[1]:
        return common[-1] +common[1]-common[0]
    # (2)
    return common[-1] * common[1]/common[0]