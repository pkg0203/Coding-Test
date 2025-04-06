"""
https://www.acmicpc.net/problem/4153

[ Geometrics ]

a,b,c의 크기가 순서대로 주어질지 모르기 때문에 정렬이 필요 ··· (1)

"""

import sys

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a==b==c==0:
        break
    # (1)
    tr = sorted([a,b,c])
    
    if tr[0]**2 + tr[1]**2 == tr[2]**2:
        sys.stdout.write("right\n")
    else:
        sys.stdout.write("wrong\n")
