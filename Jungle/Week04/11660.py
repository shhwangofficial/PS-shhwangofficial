import sys
a, b = map(int, sys.stdin.readline().split())

sequence = list(map(int, sys.stdin.readline().split()))
sequence.sort()  # 1,7,8,9

def recur(arr, i):
    if len(arr) == b:
        print(*arr)
        return
    for j in range(i, len(sequence)):
        recur(arr + [sequence[j]], j)
    return
    
for i in range(len(sequence)):
    recur([sequence[i]], i)
    