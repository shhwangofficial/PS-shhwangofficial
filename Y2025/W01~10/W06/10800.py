import sys

N = int(sys.stdin.readline())
balls = []
color_set = set([])
for i in range(N):
    C, S = map(int, sys.stdin.readline().split())
    balls.append((S, C, i))
    color_set.add(C)
balls.sort()

max_color = max(color_set)
colored_table = [0] * (max_color + 1)

total_size_sum = 0
tmp_max = 0
tmp_sum = 0
tmp = []
ans = [0] * N
for ball in balls:
    if ball[0] > tmp_max:
        for t in tmp:
            ans[t[2]] = total_size_sum - colored_table[t[1]]
        for t in tmp:
            total_size_sum += t[0]
            colored_table[t[1]] += t[0]
        tmp_max = ball[0]
        tmp = [ball]
    else:
        tmp.append(ball)

for t in tmp:
    ans[t[2]] = total_size_sum - colored_table[t[1]]

for i in ans:
    print(i)
