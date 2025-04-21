import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
HP = input()
taken = [0] * N
for i in range(N):
    if HP[i] == "P":
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if HP[j] == "H" and taken[j] == 0:
                taken[j] = 1
                break

print(sum(taken))
