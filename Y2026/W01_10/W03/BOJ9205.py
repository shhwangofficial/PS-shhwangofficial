T = int(input())
for _ in range(T):
    num = int(input())
    points = []
    for i in range(num + 2):
        x, y = map(int, input().split())
        points.append((x, y))
    matrix = [[0] * (num + 2) for _ in range(num + 2)]
    for i in range(num + 2):
        for j in range(num + 2):
            if i == j:
                continue
            if abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) <= 1000:
                matrix[i][j] = 1

    visited = [0] * (num + 2)
    from collections import deque

    queue = deque()
    queue.append(0)
    visited[0] = 1
    while queue:
        cur = queue.popleft()
        if cur == num + 1:
            print("happy")
            break
        for i in range(num + 2):
            if matrix[cur][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    else:
        print("sad")
