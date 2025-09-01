import sys


length, width, height = map(int, sys.stdin.readline().split())
total = length * width * height
cubes = []
for i in range(int(input())):
    cubes.append(list(map(int, sys.stdin.readline().split())))
cubes.sort(reverse=True)

ans, total_now = 0, 0
for cube_idx, cube_cnt in cubes:
    total_now *= 8
    cube_len = 2**cube_idx
    limit = (length // cube_len) * (width // cube_len) * (height // cube_len) - total_now
    limit = min(limit, cube_cnt)
    total_now += limit
    ans += limit

if total_now == total:
    print(ans)
else:
    print(-1)
