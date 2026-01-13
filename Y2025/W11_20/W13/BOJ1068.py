import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree_lst = list(map(int, input().split()))
deleted = int(input())


def dfs(node):
    flag = 0
    for nxt in graph[node]:
        dfs(nxt)
        flag = 1
    if not flag:
        global leaf_total
        leaf_total += 1


graph = [[] for i in range(N)]
start = -1
for i in range(N):
    if i == deleted:
        pass
    elif tree_lst[i] >= 0:
        graph[tree_lst[i]].append(i)
    else:
        start = i
if start == -1:
    print(0)
else:
    leaf_total = 0
    dfs(start)
    print(leaf_total)
