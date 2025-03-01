"""
https://www.acmicpc.net/problem/25192

"""

import sys

N = int(sys.stdin.readline())
answer = 0
people = {}
for _ in range(N):
    msg = sys.stdin.readline()[:-1]
    if msg == 'ENTER':
        people = {}
    else:
        if not people.get(msg):
            people[msg] = 1
            answer += 1
sys.stdout.write(f"{answer}")
