import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
two = [0, 0, 1, 1]
three = [0, 0, 0, 1]
for _ in range(T):
    n = int(input())
    if n <= len(two) - 1:
        print(1 + two[n] + three[n])
        continue
    while n > len(two) - 1:
        three.append(1 + two[-3] + three[-3])
        two.append(1 + two[-2])
    print(1 + two[n] + three[n])
