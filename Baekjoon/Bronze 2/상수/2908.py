# https://www.acmicpc.net/problem/2908

import sys

A, B = sys.stdin.readline().split()
max_val = max(int(A[::-1]), int(B[::-1]))
sys.stdout.write(f"{max_val}")
