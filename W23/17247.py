import sys
a, b = map(int,sys.stdin.readline().split())
lst = []
for i in range(a):
    lst.append(list(map(int, sys.stdin.readline().split())))

result = []
for i in range(a):
    for j in range(b):
        if lst[i][j] == 1:
            result.append([i, j])

print(abs(result[0][0]-result[1][0]) + abs(result[0][1]-result[1][1]))
