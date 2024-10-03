"""
https://www.acmicpc.net/problem/2798

[ Brute Force ]

먼저 입력을 받는다 ··· (1)

큰 카드부터 선택하기 위해 내림차순 정렬을 한다 ··· (2)

카드를 선택하거나, 선택하지 않는 경우를
재귀 함수로 구현한다 ··· (3)

현재 카드를 추가해도 limit를 넘지 않으면 선택 ··· (4)

선택하지 않는 경우도 구현 ··· (5)

3장을 골랐다면 candidate_answer에 추가하고
전부 선택하지 않는 경우도 탈출 조건을 구현 ··· (6)

candidate_answer 에서 가장 큰 값이 답이다 ··· (7)
"""

import sys

def find_sol(walker=0,selected=0,selected_card = []):
    # (6)
    if selected == 3:
        candidate_answer.append(sum(selected_card))
        return
    
    if walker == len(cards):
        return
    
    # (4)
    if sum(selected_card) + cards[walker] <= limit:
        selected_card.append(cards[walker])
        find_sol(walker+1,selected+1,selected_card)
        selected_card.pop()

    # (5)
    find_sol(walker+1,selected,selected_card)


# (1)
n,limit = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
# (2)
cards.sort(reverse=True)
candidate_answer = []
# (3)
find_sol()
# (7)
sys.stdout.write(f"{max(candidate_answer)}")
