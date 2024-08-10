# https://www.acmicpc.net/problem/18258

import sys
from collections import deque

Queue = deque()

T = int(sys.stdin.readline())
for testcase in range(T):
    order_list = list(map(str, sys.stdin.readline().split()))
    if len(order_list) == 2:
        Queue.append(int(order_list[1]))

    else:
        order = order_list[0]
        if order == "pop":
            if Queue:
                sys.stdout.write(f"{Queue.popleft()}\n")
            else:
                sys.stdout.write(f"-1\n")
        elif order == "size":
            sys.stdout.write(f"{len(Queue)}\n")
        elif order == "empty":
            if Queue:
                sys.stdout.write(f"0\n")
            else:
                sys.stdout.write(f"1\n")
        elif order == "front":
            if Queue:
                sys.stdout.write(f"{Queue[0]}\n")
            else:
                sys.stdout.write(f"-1\n")
        elif order == "back":
            if Queue:
                sys.stdout.write(f"{Queue[-1]}\n")
            else:
                sys.stdout.write(f"-1\n")
