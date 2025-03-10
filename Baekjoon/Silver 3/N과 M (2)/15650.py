"""
https://www.acmicpc.net/problem/15650

[ BackTracking ]
"""

def print_comb(N,M,level=1):
    if len(comb) == M:
        sys.stdout.write(f"{' '.join(comb)}\n")
        return
    
    for num in range(level,N+1):
        comb.append(str(num))
        print_comb(N,M,num+1)
        comb.pop()


import sys

N,M = map(int,sys.stdin.readline().split())
comb = []
print_comb(N,M)