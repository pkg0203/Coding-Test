# https://www.acmicpc.net/problem/9251

import sys


def find_substring(walker=0, start_idx=0):
    global answer
    # Base case
    if walker == LEN_A:
        return None

    matched = False
    for idx in range(start_idx, LEN_B):
        if A[walker] == B[idx]:
            answer.append(A[walker])
            next_idx = idx + 1
            matched = True
            break

    if matched:
        find_substring(walker + 1, next_idx)
    else:
        find_substring(walker + 1, start_idx)


# 개행 문자 때문에 마지막은 빼고 담아야 함
A = sys.stdin.readline()[:-1]
B = sys.stdin.readline()[:-1]
LEN_A, LEN_B = len(A), len(B)

answer = []
find_substring()
sys.stdout.write(f"{len(answer)}")

# 반례
# XMJYAUZ
# MZJAWXU
