# https://www.acmicpc.net/problem/12789

import sys
from collections import deque

N = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))
line = deque()
wait = deque()
for i in range(len(input)):
    line.append(input[i])
turn = 1
# line에서 wait은 갈 수 있어도
# wait에서 line은 갈 수 없다.
while turn <= N:
    if turn in line:
        if line[0] == turn:
            line.popleft()
            turn += 1
        else:
            wait.append(line.popleft())
    elif turn in wait:
        if wait[-1] == turn:
            wait.pop()
            turn += 1
        else:
            break
# while을 전부 정상적으로 돈 경우
if turn > N:
    sys.stdout.write("Nice")
else:
    sys.stdout.write("Sad")
