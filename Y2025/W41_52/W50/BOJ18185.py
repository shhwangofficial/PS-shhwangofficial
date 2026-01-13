import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
num = list(map(int, input().split()))
ans = 0
i = 0
while i < N:
    if i < N - 2 and num[i] and num[i + 1] and num[i + 2]:
        if num[i + 2] >= num[i + 1]:
            val = min(num[i], num[i + 1], num[i + 2])
            ans += val * 7
            num[i] -= val
            num[i + 1] -= val
            num[i + 2] -= val
        else:
            val = min(num[i], num[i + 1] - num[i + 2])
            ans += val * 5
            num[i] -= val
            num[i + 1] -= val
            continue
    if i < N - 1 and num[i] and num[i + 1]:
        val = min(num[i], num[i + 1])
        ans += val * 5
        num[i] -= val
        num[i + 1] -= val
    if num[i]:
        ans += num[i] * 3
    i += 1

print(ans)
