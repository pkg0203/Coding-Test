"""
https://www.acmicpc.net/problem/2805

[ Binary Search ]

절단기의 길이는 mid로 설정한다 ··· (1)

설정한 mid에 대해 상근이가 가져가는 나무는 get에 저장한다 ··· (2)

get이 M보다 큰 경우는 너무 많이 가져간 경우이다
이 경우는 절단기의 길이가 낮은 것이므로 절단기의 길이를 높이기 위해
mid 오른쪽을 탐색한다  ··· (3)

get이 M보다 작은 경우는 적게 가져간 경우이다
이 경우는 절단기의 길이가 높은 것이므로 절단기의 길이를 낮추기 위해
mid 왼쪽을 탐색한다  ··· (4)
"""

import sys

N,M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
l = 0
r = max(trees)
while l<=r:
    # (1)
    mid = (l+r)//2
    # (2)
    get = 0
    for tree in trees:
        if tree > mid:
            get += (tree-mid)
    # (3)
    if get >= M :
        l = mid +1
    # (4)
    elif get < M :
        r = mid-1
sys.stdout.write(f"{r}")