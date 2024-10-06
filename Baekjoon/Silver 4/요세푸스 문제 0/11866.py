"""
https://www.acmicpc.net/problem/11866
[ Stack & Queue ]

Stack이나 Queue로 푸는 것으로 분류되어 있는데
list로 푸는게 좀 더 직관적인 것 같다.
circle을 walker가 계속 돌게 된다.

0이 아닌 원소를 만나면 passed가 증가 ··· (1)

passed가 K-1이라면 K번째 원소이므로 answer에 추가한다
그리고 그 원소는 circle에서 0으로 바꾸고
poped를 1 증가시킨다 ··· (2)

walker가 계속 돌게하기 위해 N으로 나머지 연산을 실행한다 ··· (3)

마지막으로 join을 시행하기 위해 answer에 담긴 값들을 전부 string으로 바꿔주면 되는데
처음부터 answer.append(str(circle[walker])) 로 구현할 걸 그랬다 ··· (4)
"""

import sys

N,K = map(int,sys.stdin.readline().split())
circle = [_ for _ in range(1,N+1)]
answer = []
walker = K-1
passed = K-1
poped = 0

while poped < N :
    if circle[walker] != 0 :
        # (1)
        if passed != K-1 :
            passed += 1
        # (2)
        else :
            passed = 0
            answer.append(circle[walker])
            circle[walker] = 0
            poped += 1
    # (3)
    walker += 1
    walker %= N
# (4)
sys.stdout.write(f"<{', '.join(list(map(str,answer)))}>")