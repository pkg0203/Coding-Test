# https://www.acmicpc.net/problem/9251

import sys


def find_substring(walker=0, start_idx=0):
    global answer
    # Base case
    if walker == LEN_A:
        len_str = len(string)
        if len_str > answer:
            answer = len_str
        return None

    matched = False
    for idx in range(start_idx, LEN_B):
        if A[walker] == B[idx]:
            string.append(A[walker])
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

answer = 0
for i in range(LEN_A):
    string = []
    find_substring(walker=i)
sys.stdout.write(f"{answer}")

# 반례
# XMJYAUZ
# MZJAWXU
