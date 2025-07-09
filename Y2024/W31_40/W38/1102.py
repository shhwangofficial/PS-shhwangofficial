import sys

INF = 10**5
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

YN = sys.stdin.readline().strip()
start = 0
for i in range(len(YN)):
    if YN[i] == "Y":
        start += 2 ** (i)

get_fixed = int(sys.stdin.readline())
min_ = INF

dp = [INF] * (2**N)


def solve(visited, val):
    cnt = 0
    s = set({})
    for ones in range(N):
        if visited & (1 << ones) >= 1:
            s.add(ones)
            cnt += 1

    if cnt >= get_fixed:
        global min_
        if min_ > val:
            min_ = val
        return
    else:
        for zeros in set(range(N)) - s:
            local_min = INF
            for ones in s:
                if local_min > graph[ones][zeros]:
                    local_min = graph[ones][zeros]
            if dp[visited | (1 << zeros)] > val + local_min:
                dp[visited | (1 << zeros)] = val + local_min
                solve(visited | (1 << zeros), val + local_min)


solve(start, 0)
print(-1 if min_ == INF else min_)
