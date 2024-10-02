import sys

N = int(sys.stdin.readline())

edges = [0] + list(map(int, sys.stdin.readline().split()))
max_below = [0] * len(edges)
max_ = 0


def dfs(idx):
    left_child = 2 * idx + 1
    right_child = 2 * idx + 2

    if left_child >= len(edges):
        max_below[idx] = edges[idx]
        return max_below[idx]
    left = dfs(left_child)
    right = dfs(right_child)
    max_below[idx] = max(max_below[left_child], max_below[right_child]) + edges[idx]
    return max_below[idx]


def solve(val, idx):
    left_child = 2 * idx + 1
    right_child = 2 * idx + 2

    edges[left_child] += val - max_below[left_child]
    edges[right_child] += val - max_below[right_child]

    if 2 * right_child + 2 < len(edges):
        solve(val - edges[left_child], left_child)
        solve(val - edges[right_child], right_child)


dfs(0)
solve(max_below[0], 0)
print(sum(edges))
