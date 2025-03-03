"""
https://www.acmicpc.net/problem/24060

https://interrobang.tistory.com/90

[ Recursion ]

"""


def merge(A, p, q, r):
    global count, value
    i, j = p, q + 1
    temp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1

    while i <= q:
        temp.append(A[i])
        i += 1
    while j <= r:
        temp.append(A[j])
        j += 1

    i, t = p, 0
    while i <= r:
        A[i] = temp[t]
        count += 1
        if count == K:
            value = A[i]
            break
        i += 1
        t += 1



def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
count = 0
value = -1
merge_sort(A, 0, len(A) - 1)

sys.stdout.write(f"{value}")
