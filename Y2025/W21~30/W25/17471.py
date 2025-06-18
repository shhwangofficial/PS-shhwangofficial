import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()


from collections import deque

N = int(input())
people = [0] + list(map(int, input().split()))
total = sum(people)
graph = [[]]
for _ in range(1, N + 1):
    n, *args = map(int, input().split())
    graph.append(args)
ans = float("inf")
my_set = set()


def bfs(set_):
    if not set_:
        return False
    rep = list(set_)[0]
    queue = deque([rep])
    visited = [0] * (N + 1)
    visited[rep] = 1
    popul = 0
    while queue:
        now = queue.popleft()
        popul += people[now]
        for nxt in graph[now]:
            if nxt in set_ and not visited[nxt]:
                visited[nxt] = 1
                queue.append(nxt)
    for i in set_:
        if not visited[i]:
            return 0
    return popul


def divide():
    other_set = set(i for i in range(1, N + 1)) - my_set
    pop1 = bfs(my_set)
    pop2 = bfs(other_set)
    if pop1 and pop2:
        global ans
        ans = min(ans, abs(pop1 - pop2))


def choose(now):
    global my_set
    if len(my_set) > N // 2:
        return
    for i in range(now + 1, N + 1):
        my_set.add(i)
        divide()
        choose(i)
        my_set.discard(i)


choose(0)

print(ans if ans != float("inf") else -1)
