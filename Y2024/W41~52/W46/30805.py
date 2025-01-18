import sys

N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))


find = 100
start_1 = -1
start_2 = -1
ans = []
while find > 0:
    for i in range(start_1 + 1, N):
        if arr1[i] == find:
            for j in range(start_2 + 1, M):
                if arr2[j] == find:
                    start_2 = j
                    start_1 = i
                    ans.append(find)
                    break
    find -= 1

print(len(ans))
print(*ans)
