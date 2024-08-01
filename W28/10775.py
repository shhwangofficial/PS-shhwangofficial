import sys
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

p = [i for i in range(G+1)]

def doit(num):
    temp = num
    while p[temp] != temp:
        if p[temp] == 0:
            return True
        temp = p[temp]
    p[temp] -= 1
    p[num] = p[temp]

cnt = 0
for _ in range(P):
    gi = int(sys.stdin.readline())
    if doit(gi):
        break
    else:
        cnt += 1
   

print(cnt)