"""
https://www.acmicpc.net/problem/11689

[ Numer Theory ]

오일러 파이 함수를 구현하는 문제이다
N과 서로소의 개수를 구해주는 함수인데,
N의 소인수를 알아야 하므로 이를 factors에 담아준다
이 때 중복으로 담기지 않도록 set으로 정의한다 ··· (1)
"""

def Euler_Phi(N):
    result = N
    for p in list(factors):
        result -= result/p
    #     print(result)
    # print(factors)
    return int(result)

import sys

N = int(sys.stdin.readline())
temp = N
walker = 2
# (1)
factors = set()
while walker*walker <= N:
    if temp % walker == 0:
        factors.add(walker)
        temp //= walker
    else:
        walker += 1
if temp > 1 :
    factors.add(temp)
answer = Euler_Phi(N)
sys.stdout.write(f"{answer}")