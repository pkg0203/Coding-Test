"""
https://www.acmicpc.net/problem/15652

[ Back Tracking ]

"""

def print_inc_seq(N,M,pr_el=1):
    global arr
    if len(arr) == M:
        sys.stdout.write(f"{' '.join(arr)}\n")
        return
    
    for i in range(pr_el,N+1):
        arr.append(str(i))
        print_inc_seq(N,M,i)
        arr.pop()

import sys

N,M = map(int,sys.stdin.readline().split())
arr = []
print_inc_seq(N,M)
