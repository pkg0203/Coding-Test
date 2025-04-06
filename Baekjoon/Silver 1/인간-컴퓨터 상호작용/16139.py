"""
https://www.acmicpc.net/problem/16139

[ Prefix Sum ]

Memo[i][j] : S의 i번째 substring까지 j번째 alphabet이 나온 횟수 ··· (1)

예제와 같이 입력이 들어왔을 때, Memo[2][0]는 두 번째까지인
'se'까지에서 첫 번째 알파벳 'a'가 나온 횟수이다 ··· (2)

[:]를 붙이는 이유는 리스트의 복제를 하기 위함 ··· (3)
"""

import sys

S = sys.stdin.readline().rstrip()
questions = int(sys.stdin.readline())
# (1)
Memo = [[0 for j in range(26)]]

# (2)
for i,alphabet in enumerate(S):
    askii = ord(alphabet) - 97
    # (3)
    Memo.append(Memo[len(Memo) - 1][:])
    Memo[i+1][askii] += 1


for question in range(questions):
    alpha,l,r = map(str,sys.stdin.readline().split())
    l,r = int(l),int(r)
    askii = ord(alpha)-97
    sys.stdout.write(f"{Memo[r+1][askii]-Memo[l][askii]}\n")