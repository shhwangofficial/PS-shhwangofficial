import sys

N = int(sys.stdin.readline())
mp, mf, ms, mv = map(int, sys.stdin.readline().split())

min_cost = 9999
foods = []
ans = 0
for _ in range(N):
    foods.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, (1 << N)):
    sum_p, sum_f, sum_s, sum_v, sum_c = [0, 0, 0, 0, 0]
    for j in range(N):
        if i & (1 << j):
            sum_p += foods[j][0]
            sum_f += foods[j][1]
            sum_s += foods[j][2]
            sum_v += foods[j][3]
            sum_c += foods[j][4]
    if sum_p >= mp and sum_f >= mf and sum_s >= ms and sum_v >= mv:
        if min_cost > sum_c:
            min_cost = sum_c
            ans = [i]
        elif min_cost == sum_c:
            ans.append(i)

if ans == 0:
    print(-1)
else:
    print(min_cost)
    final = []
    for a in ans:
        temp = []
        for j in range(N):
            if a & (1 << j):
                temp.append(j + 1)
        final.append(temp)
    final.sort()
    print(*final[0])
