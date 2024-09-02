"""
https://school.programmers.co.kr/learn/courses/30/lessons/120956

[코딩테스트 입문]

만약 가능한 단어라면 답을 1 더한다 ··· (1)

단어를 2글자 또는 3글자를 자르고
그 단어가 BABBLING에 있으면 계속 진행한다 ··· (2)

만약 2글자와 3글자 모두 통과하지 못 하면 불가능한 단어이다 ··· (3)

계속 진행하다가 단어 끝까지 진행하면 (while문을 탈출하면)
가능한 단어이다 ··· (4)
"""


BABBLING = ["aya","ye","woo","ma"]

def is_possible(word):
    Aswitch,Bswitch = False,False
    walker = 0
    while walker!=len(word):
        # (2)
        if word[walker:walker+2] in BABBLING:
            walker+=2
            continue
        if word[walker:walker+3] in BABBLING:
            walker+=3
            continue
        # (3)
        if not (Aswitch and Bswitch) :
            return False
    # (4)    
    return True
        

def solution(babbling):
    answer = 0
    for word in babbling:
        # (1)
        if is_possible(word):
            answer+=1
    return answer