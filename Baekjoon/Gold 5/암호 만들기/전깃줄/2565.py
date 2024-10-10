"""
https://www.acmicpc.net/problem/2565
[ Dynamic Programming ]

A를 정의역 B를 치역으로 고려하고 전깃줄을 
함수 간의 대응 관계로 볼 때, 감소 함수이면
-> x는 증가하는데 y는 감소
선이 교차할 수 밖에 없다
따라서 증가함수가 되도록 해야한다.

정의역을 기준으로 정렬한 후에
치역만 보면 LIS 문제와 같아진다 ··· (1)

단 가장 긴 sequence의 길이 = 남아 있는 전선의 개수 이므로
제거해야할 전선 = 전체 - 가장 긴 sequence의 길이이다 ··· (2)
"""

import sys

N = int(sys.stdin.readline())

function = []

dp_incr = [ 1 for _ in range(N) ]

for _ in range(N):
    function.append(list(map(int,sys.stdin.readline().split())))
# (1)
function.sort(key=lambda x:x[0])

for i in range(1,N):
    for j in range(i):
        if function[i][1] > function[j][1]:
            dp_incr[i] = max(dp_incr[i],dp_incr[j]+1)
# (2)
answer = N - max(dp_incr)
sys.stdout.write(f"{answer}")
