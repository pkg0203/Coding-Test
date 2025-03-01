"""
https://www.acmicpc.net/problem/24511

[ Queue & Stack ]
"""

import sys
from collections import deque

N = int(sys.stdin.readline())
is_stack = list(map(int,sys.stdin.readline().split()))
elements = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
push_elements = list(map(int,sys.stdin.readline().split()))
answer = []
q = deque()
for i in range(N):
    if not is_stack[i]:
        q.appendleft(elements[i])

for push_element in push_elements:
    q.append(push_element)
    answer.append(str(q.popleft()))
sys.stdout.write(f"{' '.join(answer)}")