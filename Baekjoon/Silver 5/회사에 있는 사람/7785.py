"""
https://www.acmicpc.net/problem/7785
[ HashMap ]
state가 leave이면 list에서 삭제 ··· (1)

enter라면 list에 append한다 ··· (2)

이후 사전 역순으로 정렬한다 ··· (3)
"""

import sys

def pop_or_push(name,state):
    # (1)
    if state == "leave":
        del company_dict[name]
    # (2)
    else :
        company_dict[name] = 1

N = int(sys.stdin.readline())
company_dict = {}
for i in range(N):
    order = sys.stdin.readline()
    name = order.split()[0]
    state = order.split()[1]
    pop_or_push(name,state)
# (3)
company = sorted(company_dict.keys(),reverse=True)

for person in company:
    sys.stdout.write(f"{person}\n")

