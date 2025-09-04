def solution(land):
    from collections import deque

    r = len(land)
    c = len(land[0])
    dic = dict()
    answer = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def pipe(col):
        ret = 0
        set_ = set()
        for row in range(r):
            if visited[row][col] != 0 and visited[row][col] not in set_:
                set_.add(visited[row][col])
                ret += dic[visited[row][col]]
        return ret

    visited = [[0] * c for _ in range(r)]
    v_idx = 1
    for row in range(r):
        for col in range(c):
            if visited[row][col] == 0 and land[row][col] == 1:
                queue = deque([(row, col)])
                visited[row][col] = v_idx
                ret = 0
                while queue:
                    x, y = queue.popleft()
                    ret += 1
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and land[nx][ny] == 1:
                            queue.append((nx, ny))
                            visited[nx][ny] = v_idx
                dic[v_idx] = ret
                v_idx += 1

    for col in range(c):
        answer = max(pipe(col), answer)

    return answer
