"""
https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
[ HashMap ]

포켓몬 도감을 만든다.
등록돼 있으면 1을 더하고 아니면 1로 초기화 한다 ··· (1)

이후 키들을 모은다.
키의 종류가 곧 포켓몬의 종류인데 최대 선택 수보다 많으면 
최대 선택 수가 답이고, 아니면 키의 종류가 답이다 ··· (2)

"""



Pocketmon_Dict = {}

def solution(nums):
    answer = 0
    # (1)
    for num in nums:
        if Pocketmon_Dict.get(str(num)):
            Pocketmon_Dict[str(num)] += 1
        else :
            Pocketmon_Dict[str(num)] = 1
    # (2)
    return min(len(Pocketmon_Dict.keys()),len(nums)/2)