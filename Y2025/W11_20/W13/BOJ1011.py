import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    diff = y - x
    s, e = 1, 2**31
    while s <= e:
        mid = (s + e) // 2
        if diff <= mid**2:
            temp = mid
            e = mid - 1
        elif diff <= mid**2 + mid:
            print(2 * mid)
            break
        else:
            s = mid + 1
    else:
        print(2 * temp - 1)
