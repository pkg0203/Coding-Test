# https://www.acmicpc.net/problem/1068

import sys


def left(idx):
    return 2 * idx + 1

def make_tree():
    pass
nodes = int(sys.stdin.readline())
relations = list(map(int, sys.stdin.readline().split()))
tree = [0] + [-1 for _ in range(2**50 - 1)]
for idx in range(1, len(relations)):
    value = idx
    par_left_idx = left(tree.index(relations[idx]))
    if tree[par_left_idx] == -1:
        tree[par_left_idx] = value
    else:
        par_right_idx = par_left_idx + 1
        tree[par_right_idx] = value
print(tree[:100])
deleted_node = int(sys.stdin.readline())
# traverse()
