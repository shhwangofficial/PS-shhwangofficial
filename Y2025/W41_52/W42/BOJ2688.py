import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
lst = [[1] * 10 for _ in range(2)]
for t in range(T):
    n = int(input())
    if n >= len(lst):
        for i in range(n - len(lst) + 1):
            tmp = lst[-1][:]
            for i in range(9 - 1, -1, -1):
                tmp[i] += tmp[i + 1]
            lst.append(tmp)

    print(sum(lst[n]))
