import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

min_val = 10**9
sum_val = 0
for i in range(N - 1):
    min_val = min(min_val, cost[i])
    sum_val += min_val * road[i]

print(sum_val)
