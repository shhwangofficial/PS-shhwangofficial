import sys
T = int(sys.stdin.readline())

def lcm(a, b):
    i = a
    while True:
        if i % a == 0 and i % b == 0:
            return i
        i += a

for _ in range(T):
    M, N, x, y = map(int,sys.stdin.readline().split())
    if M == x:
        x = 0
    if N == y:
        y= 0
    if x == 0 and y == 0:
        print(lcm(M,N))
    else:
        for i in range(x,lcm(M,N)+1, M):
            if i % M == x and i % N == y:
                print(i)
                break
        else:
            print(-1)