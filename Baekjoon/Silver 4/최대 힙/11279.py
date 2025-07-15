"""
https://www.acmicpc.net/problem/11279

[ Priority Queue ]

기본적으로 제공되는 heap은 min-heap이기 때문에
max-heap을 이용하기 위해서는 원소를 음수로 저장하고 ··· (1)

pop할 때 -부호를 붙여서 출력하면 된다 ··· (2)
"""

import sys
import heapq

N = int(sys.stdin.readline())
h = []
heapq.heapify(h)

for _ in range(N):
    input = int(sys.stdin.readline())
    # (1)
    if input:
        heapq.heappush(h, -input)
    else:
        if h:
            # (2)
            sys.stdout.write(f"{-heapq.heappop(h)}\n")
        else:
            sys.stdout.write("0\n")
