import sys

N = int(sys.stdin.readline())

corners = set()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    end = (x, y)
    pivot = (x + dx[d], y + dy[d])
    lst = set((end, pivot))

    while g >= 1:
        new_lst = set()
        for point in lst:
            new_point = (pivot[0] + pivot[1] - point[1], pivot[1] + point[0] - pivot[0])
            if point == end:
                new_pivot = new_point
            new_lst.add(new_point)
        pivot = new_pivot
        lst = lst.union(new_lst)
        g -= 1
    corners = corners.union(lst)


ans = 0
for i in range(101):
    for j in range(101):
        if (i, j) in corners and (i + 1, j) in corners and (i, j + 1) in corners and (i + 1, j + 1) in corners:
            ans += 1
print(ans)
