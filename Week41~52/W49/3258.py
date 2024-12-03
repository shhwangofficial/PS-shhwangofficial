import sys

N, Z, M = map(int, sys.stdin.readline().split())

traps = set(list(map(int, sys.stdin.readline().split())))

i = 1
while i <= N:
    now = 1
    while True:
        now = (now + i) % N
        if now == 0:
            now = N

        if now == 1:
            break
        elif now in traps:
            break
        elif now == Z:
            print(i)
            exit()

    i += 1
