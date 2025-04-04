import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

knap = [0] * 100

for i in range(N):
    for k in range(len(knap) - 1, -1, -1):
        if knap[k] > 0 or k == 0:
            if k + hp[i] < 100:
                knap[k + hp[i]] = max(knap[k + hp[i]], knap[k] + happy[i])

print(max(knap))
