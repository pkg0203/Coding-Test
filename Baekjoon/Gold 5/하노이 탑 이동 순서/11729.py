"""
https://www.acmicpc.net/problem/11729

[ Recursion ]

그 위에 K-1개를 2번으로 옮겨야 ··· (1)

맨 마지막 원판을 3번으로 옮길 수 있다 ··· (2)

그 후 2번에 있는 K-1개를 다시 3번으로 옮겨준다 ··· (3)

"""

def Hanoi(K,st=1,en=3,oth=2):
    # base case
    if K <= 0:
        return
    # (1)
    Hanoi(K-1,st=st,en=oth,oth=en)
    # (2)
    sys.stdout.write(f"{st} {en}\n")
    # (3)
    Hanoi(K-1,st=oth,en=en,oth=st)


import sys

K = int(sys.stdin.readline())
sys.stdout.write(f"{2**K-1}\n")
Hanoi(K)