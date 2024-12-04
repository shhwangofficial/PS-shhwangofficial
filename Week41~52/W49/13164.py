import sys

N, K = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

sub = [num[i + 1] - num[i] for i in range(len(num) - 1)]
sub.sort()

ans = 0
for i in range(N - K):
    ans += sub[i]

print(ans)
