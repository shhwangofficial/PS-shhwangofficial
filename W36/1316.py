import sys

N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    dic = dict()
    string = sys.stdin.readline().rstrip()
    now = string[0]
    for i in string:
        if i in dic.keys() and now != i:
            break
        else:
            now = i
            dic[i] = 1
    else:
        cnt += 1

print(cnt)
