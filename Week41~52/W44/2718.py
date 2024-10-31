import sys

T = int(sys.stdin.readline())

total = [1, 1, 5]
unique = [1, 1, 4]

for _ in range(T):
    N = int(sys.stdin.readline())
    if N < len(total):
        print(total[N])
        continue

    idx = len(unique)
    while N >= idx:
        if idx > len(unique) - 1:
            u = 2 if idx % 2 else 3
            unique.append(u)

        temp = 0
        for i in range(len(total)):
            temp += total[i] * unique[-i - 1]

        total.append(temp)
        idx += 1
    print(total[N])
