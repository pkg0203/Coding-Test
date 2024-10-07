"""
https://www.acmicpc.net/problem/10989
[ Sorting ]

메모리가 굉장히 적게 주어진게 특징이다
elements.sort() 했다가 바로 실패했다

elements의 index에 해당 값이 몇 개 있는지 기록하기로 했다 ··· (1)

시간을 널널하게 준 이유가 아마 나오지 않은 값도 순회하기 때문이 아닐까 싶다 ··· (2)

idx(value)를 elements에 기록된 횟수(times)만큼 print하게 된다 ··· (3)


"""

import sys

MAX_VALUE = 10000

N = int(sys.stdin.readline())
elements = [0 for _ in range(MAX_VALUE + 1)]
# (1)
for _ in range(N):
    elements[int(sys.stdin.readline())] += 1

# (2)
for idx in range(1,MAX_VALUE+1):
    for times in range(elements[idx]):
        # (3)
        sys.stdout.write(f"{idx}\n")