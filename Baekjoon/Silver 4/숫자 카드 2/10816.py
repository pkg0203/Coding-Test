"""
https://www.acmicpc.net/problem/10816
[ HashMap]

먼저 입력 받은 카드를 HashMap에 등록한다 ··· (1)

HashMap에 Matching할 카드를 입력받는다 ··· (2)

Matching된 카드가 HashMap에 있으면 값을, 없으면 0을 answer에 담아둔다 ··· (3)

answer에 담아둔 것을 공백과 함께 출력한다 ··· (4)
"""

import sys

N = int(sys.stdin.readline())

card_dict = dict()

cards = list(map(int,sys.stdin.readline().split()))
answer = []
# (1)
for card in cards :
    if card_dict.get(card) :
        card_dict[card] +=1
    else :
        card_dict[card] = 1

M = int(sys.stdin.readline())
# (2)
match =list(map(int,sys.stdin.readline().split()))

# (3)
for card in match :
    if card_dict.get(card) :
        answer.append(str(card_dict[card]))
    else :
        answer.append('0')
# (4)
sys.stdout.write(f"{' '.join(answer)}")