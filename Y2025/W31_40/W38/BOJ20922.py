import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
lst = list(map(int, input().split()))
if N == 1:
    print(1)
    exit()

i, j = 0, 1
counter = [0] * 100001
ans = 1
counter[lst[0]] += 1
while j < N:
    if counter[lst[j]] >= K:
        counter[lst[i]] -= 1
        i += 1
        if i == j:
            j += 1
        continue

    else:
        ans = max(ans, j - i + 1)
        counter[lst[j]] += 1
        j += 1
print(ans)
