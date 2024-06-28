# https://www.acmicpc.net/problem/11005

import sys

number, order = map(int, sys.stdin.readline().split())
bit = []
answer = []
while number > 0:
    bit.append(number % order)
    number //= order
bit = bit[::-1]
for i in range(len(bit)):
    if bit[i] < 10:
        answer.append(str(bit[i]))
    else:
        answer.append(chr(bit[i] + 55))

sys.stdout.write(f"{''.join(answer)}")
