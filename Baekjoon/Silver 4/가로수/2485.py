"""
https://www.acmicpc.net/problem/2485
[ Number Theroy ]

일정한 간격은 "어떤 수"의 배수로 생각할 수 있다
따라서 마지막 원소를 "그 수"로 나누면 총 나무의 개수를 알 수 있다

먼저 일괄적으로 0으로 시작하도록 입력을 평행이동으로 저장 ··· (1)

즉 trees의 원소들은 "어떤 수"의 배수가 되어야 하고
"어떤 수"는 원소들의 공통 약수인데, 나무를 최대한 적게 심어야하므로
최대 공약수를 구해준다 ··· (2)

심어야하는 나무 = 간격//최대공약수 -1으로 쓸수 있다
즉 간격이 최대공약수보다 크면 심어야하고 그렇지 않으면
안 심어도 된다 ··· (3)

---참고할만한 반례---
4
1
8
43
48
-> GCD 가 1이되는 경우
"""

def GCD(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        r = a % b
        a = b
        b = r
    return a


import sys
import math

N = int(sys.stdin.readline())
trees = []
# (1)
move = 0
for idx in range(N):
    input = int(sys.stdin.readline())
    if idx == 0:
        trees.append(0)
        move = input
    else:
        trees.append(input - move)
# (2)
distances = []
gcd = trees[-1]
for i in range(N - 1):
    distances.append(trees[i + 1] - trees[i])
    if i > 0:
        gcd =  GCD(distances[i], gcd)
# (3)
answer = 0
if gcd:
    for distance in distances:
        answer += distance // gcd - 1
sys.stdout.write(f"{answer}")

