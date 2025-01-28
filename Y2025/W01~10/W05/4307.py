T = int(input())
for t in range(T):
    l, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]
    min_ = 0
    for ant in ants:
        min_ = max(min_, min(l - ant, ant))

    a, b = min(ants), max(ants)
    max_ = max(l - a, a, l - b, b)

    print(min_, max_)
