"""
https://www.acmicpc.net/problem/11399

[ Greedy Algorithm ]

Shortest First로 구현하면 된다

"""
import sys

N = int(sys.stdin.readline())
times = list(map(int,sys.stdin.readline().split()))
times.sort()
answer = 0

for i,time in enumerate(times):
    answer += time *(N-i)
sys.stdout.write(f"{answer}")