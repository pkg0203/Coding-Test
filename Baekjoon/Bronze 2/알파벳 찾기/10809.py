# https://www.acmicpc.net/problem/10809

import sys

ASCII_OF_a = 97
ASCII_OF_z = 122

word = sys.stdin.readline()
answer = []

# 97부터 122를 돌게 됨
# a~z까지 word에서 찾고 answer에 append
for walker in range(ASCII_OF_a, ASCII_OF_z + 1):
    answer.append(str(word.find(chr(walker))))
sys.stdout.write((" ").join(answer))
