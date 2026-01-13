import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10005)
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)

id = 0
visited = [0] * (V + 1)
in_stack = [0] * (V + 1)
ans = []
stack = []


def dfs(now):
    global id
    id += 1
    visited[now] = id
    stack.append(now)
    in_stack[now] = 1
    now_id = id
    tmp = now_id
    for nxt in graph[now]:
        if not visited[nxt]:
            tmp = min(tmp, dfs(nxt))
        elif visited[nxt] and in_stack[nxt]:
            tmp = min(tmp, visited[nxt])

        # if visited[nxt] and in_stack[nxt]:
        #     tmp = min(tmp, visited[nxt])
        # else:
        #     tmp = min(tmp, dfs(nxt))

    if tmp == now_id:
        ret = []
        while stack:
            n = stack.pop()
            in_stack[n] = False
            ret.append(n)
            if n == now:
                break
        ans.append(sorted(ret))

    return tmp


for i in range(1, V + 1):
    if not visited[i]:
        dfs(i)

print(len(ans))
ans.sort()
for a in ans:
    a.append(-1)
    print(*a)
