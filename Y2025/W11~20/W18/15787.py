import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
trains = [0] * (N + 1)

for _ in range(M):
    cmd, *args = map(int, input().split())

    if cmd in (1, 2):
        no, seat = args
        if cmd == 1:
            trains[no] |= 1 << (seat - 1)
        else:
            trains[no] &= ~(1 << (seat - 1))
    else:
        no = args[0]
        if cmd == 3:
            trains[no] = (trains[no] << 1) & ((1 << 20) - 1)
        else:
            trains[no] >>= 1

print(len(set(trains[1:])))
