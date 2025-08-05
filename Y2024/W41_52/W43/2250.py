import sys

N = int(sys.stdin.readline())

graph = [[0, 0] for _ in range(N + 1)]
width = [[0, 0] for _ in range(N + 1)]
nodes = set(range(1, N + 1))
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][0], graph[a][1] = b, c
    nodes.discard(b)
    nodes.discard(c)

col = 1


def solve(node, lvl):
    if graph[node][0] != -1:
        solve(graph[node][0], lvl + 1)

    global col
    if width[lvl][0] == 0:
        width[lvl][0] = col
    else:
        width[lvl][1] = col

    col += 1

    if graph[node][1] != -1:
        solve(graph[node][1], lvl + 1)


root = list(nodes)[0]
solve(root, 1)

max_width = 0
max_lvl = 0
for i in range(N, 0, -1):
    if width[i][0] == 0 and width[i][1] == 0:
        continue
    if width[i][1] == 0:
        temp_width = 1
    else:
        temp_width = width[i][1] - width[i][0] + 1

    if temp_width >= max_width:
        max_width = temp_width
        max_lvl = i

print(max_lvl, max_width)
