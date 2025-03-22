"""
https://www.acmicpc.net/problem/14889

[ Back Tracking ]

스타트 팀과 링크 팀을 구할 때 (1,2)/(3,4) 와 (3,4)/(1,2) 는
전력차가 같기 때문에, 팀 하나를 고정해두고 이를 기준으로 생각한다 
이를 A팀이라고 하고 0번 선수를 미리 넣어둔다 ··· (1)

전체 사람을 구해두고 A팀에 없는 사람을 B팀에 넣을 예정이다 ··· (2)

A팀에 선택할 수 있는 사람을 모두 선택하면서 dfs를 진행 
pick을 사용한 이유는 한 팀에 같은 사람이 중복으로 들어가는 것을 방지하기 위함 ··· (3)

A팀과 B팀을 모두 구하고, A팀의 전력과 B팀의 전력을 계산한다 ··· (4)

전력의 차이가 기존의 값보다 작다면 update 해준다 ··· (5)

dfs에서 돌아올 때, A는 pop을 통해 원소를 제거하지만
B는 A를 모두 구했을 때 원소를 구하기 때문에 초기화는
전력 차이를 구한 뒤에 한다 ··· (6)
"""

def get_diff(A,B):
    A_power = 0
    B_power = 0
    # (4)
    for i in range(N//2):
        for j in range(i+1,N//2):
            A_power += S[A[i]][A[j]]
            A_power += S[A[j]][A[i]]
    # (4)
    for i in range(N//2):
        for j in range(i+1,N//2):
            B_power += S[B[i]][B[j]]
            B_power += S[B[j]][B[i]]
    return abs(A_power-B_power)
    
def dfs(pick=0):
    global A,B,diff
    if len(A) == N//2:
        # (2)
        for per in person:
            if not per in A:
                B.append(per)
        result = get_diff(A,B)
        # (6)
        B=[]
        # (5)
        diff = min(result,diff)
        return
    # (3)
    for i in range(pick+1,N):
        A.append(i)
        dfs(i)
        A.pop()

import sys
import math

N = int(sys.stdin.readline())
S = []
diff = math.inf
# (1)
A,B = [0],[]
for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    S.append(row)
# (2)
person = [i for i in range(N)]
dfs()
sys.stdout.write(f"{diff}\n")
