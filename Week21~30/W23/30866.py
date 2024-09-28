import sys

a, b = map(int, sys.stdin.readline().split())
for _ in range(b):
    num = set(list(map(int, sys.stdin.readline().split()))[1:])
    for i in num:
        if -i in num:
            break
    else:
        print("YES")
        ans = [0] * a
        for i in num:
            if i > 0:
                ans[i - 1] = 0
            else:
                ans[abs(i) - 1] = 1
        print(*ans)
        break

else:
    print("NO")
