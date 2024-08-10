# https://www.acmicpc.net/problem/1068


def dfs(node, tree, deleted, visited):
    if node == deleted:
        return 0
    if not tree[node]:
        return 1

    count = 0
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            count += dfs(child, tree, deleted, visited)

    if count == 0:
        return 1
    return count


def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    parents = list(map(int, data[1 : n + 1]))
    deleted_node = int(data[n + 1])

    if n == 1:
        print(0 if deleted_node == 0 else 1)
        return

    tree = [[] for _ in range(n)]
    root = -1

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    visited = [False] * n
    if root == deleted_node:
        print(0)
    else:
        result = dfs(root, tree, deleted_node, visited)
        print(result)


if __name__ == "__main__":
    main()
