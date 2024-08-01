import sys, heapq
from itertools import permutations
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A_sort = tuple(sorted(A))
set_ = set()
mydict = dict()
for i in permutations(A):
    set_.add(i)
for i in set_:
    mydict[i] = -1
mydict[tuple(A)] = 0

heap = [[0, tuple(A)]]

commands = []
M = int(sys.stdin.readline())
for _ in range(M):
    commands.append(list(map(int, sys.stdin.readline().split())))

while heap:
    now = heapq.heappop(heap)[1]
    if now == A_sort:
        
        break
    for command in commands:
        then = list(now)
        then[command[0]-1], then[command[1]-1] = then[command[1]-1], then[command[0]-1]
        then = tuple(then)
        if mydict[then] == -1 or mydict[then] > mydict[now] + command[2]:
            mydict[then] = mydict[now] + command[2]
            heapq.heappush(heap, [mydict[then], then])

print(mydict[A_sort])



        
