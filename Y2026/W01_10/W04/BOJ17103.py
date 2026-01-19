import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

prime_table = [True] * 1000001
prime_table[0], prime_table[1] = False, False
for i in range(2, int(1000000 ** (0.5)) + 1):
    if prime_table[i]:
        for j in range(i, 1000000 // i + 1):
            prime_table[i * j] = False

for t in range(T):
    N = int(input())
    cnt = 0
    for i in range(2, N // 2 + 1):
        if prime_table[i] and prime_table[N - i]:
            cnt += 1
    print(cnt)
