"""
https://school.programmers.co.kr/learn/courses/30/lessons/389479

[ Mathematics ]
"""


def solution(players, m, k):
    answer = 0
    on_server = [0 for i in range(len(players))]

    for i in range(len(players)):
        require_server = players[i] // m
        # 서버 증축이 필요한 상황
        if on_server[i] < require_server:
            adding_server = require_server - on_server[i]
            for j in range(k):
                if i + j < len(on_server):
                    on_server[i + j] += adding_server
            answer += adding_server
    return answer
