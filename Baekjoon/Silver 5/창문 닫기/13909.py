"""
https://www.acmicpc.net/problem/13909
[ Number Theory ]

i번째 창문을 기준으로 생각했을 때,
i의 약수에 해당하는 사람은 창문을 열거나 닫게된다

따라서 창문이 열려있으려면 i의 약수의 개수는 홀수여야 하고
약수의 개수가 홀수라는 것은 제곱수라는 것이다

따라서 i이하의 제곱수의 개수를 카운트하면 된다
"""

import sys

N = int(sys.stdin.readline())
answer = 0
walker = 1
while True:
    if walker**2 <=N:
        answer += 1
        walker += 1
    else:
        break

sys.stdout.write(f"{answer}\n")