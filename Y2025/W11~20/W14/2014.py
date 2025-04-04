import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

import heapq

K, N = map(int, input().split())
primes = list(map(int, input().split()))
primes.sort()
heap = primes[:]


cnt = 1
while cnt <= N:
    now = heapq.heappop(heap)
    for p in primes:
        heapq.heappush(heap, now * p)
        if now % p == 0:
            break
    cnt += 1

print(now)
