import sys
N, M, K = map(int,sys.stdin.readline().split())

num = [0] + list(map(int, sys.stdin.readline().split()))

root = [i for i in range(N+1)]

def union(v1, v2):
    r1 = find_root(v1)
    r2 = find_root(v2)

    if r1 < r2:
        root[r2] = r1
    else:
        root[r1] = r2

def find_root(v1):
    while v1 != root[v1]:
        v1 = root[v1]
        
    return v1

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    union(a, b)
    
for i in range(1, len(num)):
    root[i] = root[root[i]]

candies = dict()
kids = dict()
for i in range(1, len(num)):
    candies[root[i]] = candies.setdefault(root[i], 0) + num[i]
    kids[root[i]] = kids.setdefault(root[i], 0) + 1

dp = [0] * K
for key in kids.keys():
    for i in range(K-1, kids[key]-1, -1):
        dp[i] = max(dp[i-kids[key]] + candies[key], dp[i])

print(max(dp))
