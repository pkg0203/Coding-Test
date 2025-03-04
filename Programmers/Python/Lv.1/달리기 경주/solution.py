"""
https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3

[ Dictionary ]

hashmap[등수] = 선수
hashmap[선수] = 등수

를 유지한다.
"""

def solution(players, callings):
    answer = []
    hash_map = {}
    for i in range(len(players)):
        ranking = i+1
        hash_map[ranking] = players[i]
        hash_map[players[i]] = ranking
    
    for call in callings:
        now_rank = hash_map[call]
        fr_person = hash_map[now_rank-1]
        hash_map[call] -= 1
        hash_map[now_rank-1] = call
        hash_map[fr_person] +=1
        hash_map[now_rank] = fr_person
    
    for i in range(len(players)):
        rank = i+1
        answer.append(hash_map[rank])
    return answer