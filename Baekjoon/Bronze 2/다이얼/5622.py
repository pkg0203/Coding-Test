# https://www.acmicpc.net/problem/5622
# <Dictionary에서 For문>
# https://jsikim1.tistory.com/211

DIAL_CHAR = {
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
}

import sys

answer = 0
input_char = list(sys.stdin.readline())
for char in input_char:
    for key in DIAL_CHAR:
        if char in DIAL_CHAR[key]:
            answer += 1 + key
            break
sys.stdout.write(f"{answer}")
