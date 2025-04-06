"""
https://www.acmicpc.net/problem/10986

[ Prefix Sum ]

sums는 i번째까지의 원소의 합을 나타낸다
그런데 어차피 M으로 나눌 것이기 때문에 미리 나눠서 sums에 저장한다 ··· (1)

sum_board는 sums에 있는 원소의 개수를 담아놓은 것인데
다시 풀면서 생각해보니 rem_board가 더 맞는 명명법이지 않나 싶다 
sum_board[0] = 1 이라면 sums에는 0이라는 원소가 1개 있다는 뜻이다 ··· (2)

sums를 채우려고 처음에 0을 넣어두었는데 ··· (3)

이제 필요없으니 빼준다 ··· (4)

먼저 1개의 길이로 이루어진 원소가 M으로 나누어 떨어지면 answer에 추가해준다 ··· (5)

이제 연속하는 subsequence의 합이 M으로 나누어 떨어지려면 
i부터 j번째의 원소의 합이 M으로 나누어 떨어져야 하는데,
이는 곧 (sums[j] - sums[i-1])%M == 0 을 의미한다.

근데 이렇게 구현하면 당연히 시간 초과가 나기 때문에
sums[j] == sums[i-1] 인 것의 개수를 찾으려 한다
이를 위해 sum_board를 만든 것이다

sum_board를 돌 것인데 이 원리를 설명하면
sums[1] , sums[3], sums[5]의 값이 모두 1이라고 해보자
그러면 sum_board[1] = 3일테고, M으로 나누어 떨어지는 순서쌍은
(2,3), (4,5), (2,5)와 같이 3개로 나올 것이다
따라서 조합을 이용해서 구해주면 된다 ··· (6)
"""

import sys
import math

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
# (3)
sums = [0]
sum_board = [0 for i in range(M)]
answer = 0
# (1)
for i, num in enumerate(nums):
    value = (sums[i] + num) % M
    sums.append(value)
    # (2)
    sum_board[value] += 1
# (4)
sums = sums[1:]
# (5)
answer += sum_board[0]

# (6)
for i, val in enumerate(sum_board):
    if val:
        answer += math.comb(val, 2)

sys.stdout.write(f"{answer}")