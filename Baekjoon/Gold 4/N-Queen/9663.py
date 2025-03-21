"""
https://www.acmicpc.net/problem/9663

[ Back Tracking ]

chess의 index와 value는 queen의 위치를 나타낸다.
chess = [0,1] 이라면
chess[0] = 0 이고 chess[1]=1 이므로
(0,0) 과 (1,1)에 queen이 위치한다는 의미이다.

이렇게 설정할 경우 같은 column에 queen이 놓일 일이 없으므로
같은 row에 queen이 위치하는지 ··· (1)
같은 대각선(?) 상에 queen이 위치하는지 ··· (2)
만을 check하면 된다.

또한 유망하지 않다면 해당 level에서 dfs를 진행하지 않게 된다 ··· (3)

유망한 상태로 모든 chess판을 채웠다면, 이는 겹치지 않게 queen을 배치한 것이므로
answer의 값을 1 더해준다 ··· (4)
"""
def is_valid(idx):
    for i in range(idx):
            # (1)
            if chess[i] == chess[idx]:
                return False
            # (2)
            if idx-i == abs(chess[i]-chess[idx]):
                return False
    return True


def dfs(lv=0):
    global answer
    # base case
    # (4)
    if lv == N :
        answer +=1
        return
    
    for i in range(N):
        chess[lv] = i
        if is_valid(lv):
            # (3)
            dfs(lv+1)

import sys

N = int(sys.stdin.readline())
answer = 0
chess = [0 for _ in range(N)]
dfs()
sys.stdout.write(f"{answer}")
