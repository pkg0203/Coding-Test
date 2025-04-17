"""
https://www.acmicpc.net/problem/1931

[ Greedy Algorithm ]


가장 빨리 끝나는 회의부터 추가하면 된다

"""

import sys

N = int(sys.stdin.readline())
times = []
ex_time = 0
answer = 0

for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    times.append(row)
# 정렬 시, x[0]를 하지 않으면 반례를 통과하지 못 한다
times.sort(key=lambda x:(x[1],x[0]))

for i,[st_time,ed_time] in enumerate(times):
    if ex_time <= st_time:
        answer +=1
        ex_time = ed_time

sys.stdout.write(f"{answer}")