import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    row, col = map(int,sys.stdin.readline().split())
    map_ = [['.' for i in range(col+2)]]
    for i in range(row):
        temp = list(map(str, sys.stdin.readline().rstrip()))
        map_.append( ['.'] + temp + ['.'])
    map_.append(['.' for i in range(col+2)])
    keys = set(map(str, sys.stdin.readline().rstrip()))
    if keys == {0}:
        keys = set()
    visited = [[0 for i in range(col+2)] for j in range(row+2)]
    visited[0][0] = 1
    doc_cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque([[0,0]])
    waiting_for_key = {}
    while queue:
        now = queue.popleft()
        for i in range(4):
            new_x = now[0] + dx[i]
            new_y = now[1] + dy[i]
            if 0<=new_x<row+2 and 0<=new_y<col+2:
                if map_[new_x][new_y] != "*" and visited[new_x][new_y]==0:
                    if map_[new_x][new_y] == ".":
                        visited[new_x][new_y] = 1
                        queue.append([new_x, new_y])
                    elif map_[new_x][new_y] == "$":
                        visited[new_x][new_y] = 1
                        doc_cnt += 1
                        queue.append([new_x, new_y])
                    elif ord('a') <= ord(map_[new_x][new_y]) <= ord('z'):
                        visited[new_x][new_y] = 1
                        keys.add(map_[new_x][new_y])
                        queue.append([new_x, new_y])
                        if map_[new_x][new_y].upper() in waiting_for_key:
                            for val in waiting_for_key[map_[new_x][new_y].upper()]:
                                queue.append(val)
                    elif ord('A') <= ord(map_[new_x][new_y]) <= ord('Z'):
                        if map_[new_x][new_y].lower() in keys:
                            visited[new_x][new_y] = 1
                            queue.append([new_x, new_y])
                        else:
                            if map_[new_x][new_y] not in waiting_for_key:
                                waiting_for_key[map_[new_x][new_y]] = []
                            waiting_for_key[map_[new_x][new_y]].append([new_x, new_y])
    print(doc_cnt)
