N = int(input())

if N == 1:
    print(0)
    exit()
a, b = 0, 1
i = 3
while i <= N:
    a, b = b, (i - 1) * (a + b) % 1000000000
    i += 1
print(b)
