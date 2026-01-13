import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

D, K = map(int, input().split())
fibo = [0, 1, 1]
for i in range(3, 30):
    fibo.append(fibo[i - 1] + fibo[i - 2])

i = 1
while i <= K:
    if (K - (fibo[D - 2] * i)) % fibo[D - 1] == 0:
        print(i)
        print((K - (fibo[D - 2] * i)) // fibo[D - 1])
        break
    i += 1
