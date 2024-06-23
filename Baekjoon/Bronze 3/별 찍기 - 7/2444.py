# https://www.acmicpc.net/problem/2444

import sys


def print_star(level=1, reverse=False):
    if not reverse:
        # print Space
        for i in range(N - level):
            sys.stdout.write(" ")
        # print Star
        for i in range(2 * level - 1):
            sys.stdout.write("*")
        sys.stdout.write("\n")
        if level < N:
            print_star(level + 1)
    else:
        # print Space
        for i in range(level):
            sys.stdout.write(" ")
        # print Star
        for i in range(2 * (N-level)-1 ):
            sys.stdout.write("*")
        sys.stdout.write("\n")
        if level < N-1:
            print_star(level + 1,reverse=True)


N = int(sys.stdin.readline())
print_star()
print_star(reverse=True)
