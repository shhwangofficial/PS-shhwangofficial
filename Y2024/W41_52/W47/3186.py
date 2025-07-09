import sys

K, L, N = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().rstrip())) + (["0"] * L)

flushed = 0
i = 0
cont1 = 0
cont0 = 0
finish_pee = 0
while i < len(lst):
    if lst[i] == 1:
        cont0 = 0
        cont1 = min(cont1 + 1, K)
        if cont1 == K:
            finish_pee = 1
    else:
        cont1 = 0
        cont0 = min(cont0 + 1, L)
        if cont0 == L and finish_pee == 1:
            print(i + 1)
            flushed = 1
            finish_pee = 0
    i += 1

if not flushed:
    print("NIKAD")
