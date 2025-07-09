import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]
course = [[0] * (n + 1) for j in range(n + 1)]
for _ in range(m):
    fr, to, cst = map(int, sys.stdin.readline().split())
    graph[fr][to] = min(cst, graph[fr][to])

for i in range(1, n + 1):
    graph[i][i] = 0

for via in range(1, n + 1):
    for fr in range(1, n + 1):
        for to in range(1, n + 1):
            if graph[fr][to] > graph[fr][via] + graph[via][to]:
                graph[fr][to] = graph[fr][via] + graph[via][to]
                course[fr][to] = via


def find_course(fr, to):
    if not course[fr][to]:
        return [fr]
    return [*find_course(fr, course[fr][to]), *find_course(course[fr][to], to)]


for fr in range(1, n + 1):
    for to in range(1, n + 1):
        if graph[fr][to] == float("inf"):
            graph[fr][to] = 0

for line in graph[1:]:
    print(*line[1:])

for fr in range(1, n + 1):
    for to in range(1, n + 1):
        if fr == to or graph[fr][to] == 0:
            print(0)
        else:
            ans_course = find_course(fr, to)
            print(len(ans_course) + 1, *ans_course, to)
