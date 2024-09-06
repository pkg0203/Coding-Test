"""
https://school.programmers.co.kr/learn/courses/30/lessons/250121

[ Sort Key & Dictionary (Hash)]

ext를 기준으로 val_ext보다 작은 data를 answer에 담는다 ··· (1)

그 후, sort_by를 기준으로 answer를 정렬한다 ··· (2)
"""



import copy

IDX_DICT = {
    "code" : 0,
    "date" : 1,
    "maximum" : 2,
    "remain" : 3,
}

def solution(data, ext, val_ext, sort_by):
    answer = []
    # (1)
    for walker in data:
        if walker[IDX_DICT[ext]] < val_ext:
            answer.append(walker)
            
    # (2)
    answer.sort(key=lambda x:x[IDX_DICT[sort_by]])
    return answer