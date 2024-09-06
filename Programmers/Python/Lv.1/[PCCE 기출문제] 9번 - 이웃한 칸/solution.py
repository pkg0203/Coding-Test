"""
https://school.programmers.co.kr/learn/courses/30/lessons/250125#

[ Double Array ]

위쪽 탐색 ··· (1)

왼쪽 탐색 ··· (2)

아래쪽 탐색 ··· (3)

오른쪽 탐색 ··· (4)
"""



def solution(board, h, w):
    answer = 0
    selected_color = board[h][w]
    # (1)
    if h != 0 :
        if board[h-1][w] == selected_color:
            answer+=1
    # (2)
    if w != 0 :
        if board[h][w-1] == selected_color:
            answer+=1
    # (3)
    if h != len(board)-1 :
        if board[h+1][w] == selected_color:
            answer+=1
    # (4)        
    if w != len(board[0])-1:
        if board[h][w+1] == selected_color:
            answer +=1
    return answer