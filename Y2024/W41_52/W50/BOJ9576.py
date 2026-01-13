import sys

T = int(sys.stdin.readline())

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    books = [0] * (N + 1)
    request = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    request.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    for s, e in request:
        book = 1
        while book <= N:
            if book > e:
                break
            if s <= book <= e and not books[book]:
                ans += 1
                books[book] = 1
                break
            book += 1

    print(ans)
