"""
https://school.programmers.co.kr/learn/courses/30/lessons/42586#

[ Stack & Queue ]


먼저 각 과정과 속도 별로 며칠이 걸리는지 계산한다 ··· (1)

deploy는 배포할 개수와 기준이 되는 prior을 초기화한다 ··· (2) 

걸리는 시간이 감소하면 같이 배포하면 된다.
이 때 Queue에서 pop하게 된다 ··· (3)

그렇지 않으면 따로 배포하게 된다
즉 prior과 deploy를 초기화해주고,
현재까지 배포를 answer에 더해준다 ··· (4)
"""

import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    days = deque()
    # (1)
    for walker in range(len(speeds)):
        days.append(math.ceil((100 - progresses[walker]) / speeds[walker]))
    # (2)
    deploy = 0
    prior = days[0]
    while days:
        now = days[0]
        # (3)
        if prior >= now:
            deploy += 1
            days.popleft()
        # (4)
        else:
            answer.append(deploy)
            prior = days[0]
            deploy = 0
    answer.append(deploy)
    return answer
