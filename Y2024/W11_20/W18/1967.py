import sys

sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    parent, child, length = map(int, sys.stdin.readline().split())
    graph[parent].append([child, length])
    graph[child].append([parent, length])


def dfs(start, current_sum):
    candidate = []
    for i in range(len(graph[start])):
        if visited[graph[start][i][0]] == 0:
            visited[graph[start][i][0]] = 1
            candidate.append(
                dfs(
                    graph[start][i][0],
                    [graph[start][i][0], current_sum[1] + graph[start][i][1]],
                )
            )

    if len(candidate) == 0:
        return current_sum

    max_sum = 0
    max_node = 0
    for j in range(len(candidate)):
        if candidate[j][1] > max_sum:
            max_sum = candidate[j][1]
            max_node = candidate[j][0]

    return [max_node, max_sum]


visited = [0] * (N + 1)
visited[1] = 1
node_1 = dfs(1, [0, 0])

visited = [0] * (N + 1)
visited[node_1[0]] = 1
print(dfs(node_1[0], [0, 0])[1])
