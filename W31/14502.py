import sys
import copy
row, col = map(int,sys.stdin.readline().split())
graph = []
for i in range(row):
    graph.append(list(map(int,sys.stdin.readline().split())))

queue = []
for i in range(row):
    for j in range(col):
        if graph[i][j] == 2:
            queue.append([i,j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_ = 0

def doit():
    global max_
    temp_graph = copy.deepcopy(graph)
    temp_queue = queue[:]
    while temp_queue:
        x, y = temp_queue.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<row and 0<=ny<col and temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                temp_queue.append([nx, ny])

    temp = 0
    for i in range(row):
        for j in range(col):
            if temp_graph[i][j] == 0:
                temp += 1
    max_ = max(max_, temp)


def recur(depth, r, c):
    if depth == 3:
        return doit()
    if r >= row:
        return
    if c == col-1:
            nc = 0
            nr = r+1
    else:
        nc = c+1
        nr = r
    if graph[r][c] == 0:
        graph[r][c] = 1
        recur(depth+1, nr, nc)
        graph[r][c] = 0
    
    recur(depth, nr, nc)

    
recur(0, 0, 0)
print(max_)
