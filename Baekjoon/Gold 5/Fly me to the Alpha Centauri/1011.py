"""
https://www.acmicpc.net/problem/1011
[ Mathematics ]

시작점이나 끝점에 의존하는 것이 아니라 두 점 사이의 거리에 의존한다 ··· (1)

d = 1 : 1
d = 2 : 1 + 1
d = 3 : 1 + 1 + 1
d = 4 : 1 + 2 + 1
---
d = 5 : 1 + 2 + 1 + 1
d = 6 : 1 + 2 + 2 + 1
d = 7 : 1 + 2 + 2 + 1 + 1
d = 8 : 1 + 2 + 2 + 2 + 1

d = 9 : 1 + 2 + 3 + 2 + 1
---
.
.
d = 16 : 1 + 2 + 3 + 4 + 3 + 2 + 1
로 d가 제곱수이면 순차적으로 증가해서 순차적으로 감소하게 된다
그래서 이를 기점으로 생각한다

먼저 d가 제곱수인지 구한다.
루트를 취해서 버림을 하고 제곱했을 때, d와 같으면 제곱수이다 ··· (2)

이 경우 1부터 루트값까지 순차적으로 증가하고 감소한 개수 2k-1개이다 ··· (3)

upper는 d보다 큰 수 중 가장 작은 제곱수이고
lower는 d보다 작은 수 중 가장 큰 제곱수이다 ··· (4)

8과 같이 가까운 제곱수(9)가 위에 있으면 가까운 제곱수에 의존한다 ··· (5)

5와 같이 제곱수가 아니면 가까운 제곱수(4)가 아래에 있으면 가까운 제곱수보다 1개 많다 ··· (6)
"""

import sys


initial_dict = [None,1,2,3,3]

def get_series(k):
    return 2*k -1

def find_sol(d):
    if d<=4 :
        return initial_dict[d]
    else :
        int_root = int(d**(1/2))
        root_square = (int_root)**2

        # (2)
        if root_square == d :
            # (3)
            return get_series(int_root)
        # (4)
        else :
            lower = int_root**2
            upper = (int_root + 1)**2
            # (5)
            if upper - d < d - lower :
                return get_series(int_root+1)
            # (6)
            return get_series(int_root)+1

T = int(sys.stdin.readline())

for testcase in range(T):
    x,y = map(int,sys.stdin.readline().split())
    # (1)
    d = y-x
    sys.stdout.write(f"{find_sol(d)}\n")
