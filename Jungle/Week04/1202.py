import sys, heapq

N, K = map(int, sys.stdin.readline().split())
gems = []
for _ in range(N):
    gems.append(list(map(int, sys.stdin.readline().split())))

bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

gems.sort() 
bags.sort() 

result = 0 
tmp = [] 
 
for bag in bags:
    while gems and gems[0][0] <= bag: 
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    if tmp: 
        result -= heapq.heappop(tmp)
print(result)