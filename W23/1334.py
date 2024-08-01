import sys
n = int(sys.stdin.readline())
N = list(str(n))

if set(N)-{'9'}==set():
    print(n+2)
    exit()

idx = 0

mid1 = (len(N)-1) // 2
mid2 = len(N) // 2
while mid1 - idx >= 0:
    if N[mid1-idx] != N[mid2+idx]:
        if int(N[mid1-idx]) > int(N[mid2+idx]):
            while mid1-idx >= 0:
                N[mid2+idx] = N[mid1-idx]
                idx += 1
            break
        else:
            if N[len(N)//2] == '9':
                new = N[:(len(N)-1) // 2 +1]
                temp = ''
                for j in range(len(new)):
                    temp += new[j]
                temp = str(int(temp)+1)
                new = temp
                idx = 0
                while mid1-idx >= 0:
                    N[mid2+idx] = new[mid1-idx]
                    idx += 1
                for j in range(len(new)):
                    N[j] = new[j]
            else:
                N[len(N) // 2] = str(int(N[len(N) // 2])+1)
                if len(N) % 2 == 0:
                    N[(len(N)-1) // 2] = str(int(N[(len(N)-1) // 2])+1)
                while mid1-idx >= 0:
                    N[mid2+idx] = N[mid1-idx]
                    idx += 1
            break
    idx += 1

else:
    new = N[:(len(N)-1) // 2 +1]
    temp = ''
    for j in range(len(new)):
        temp += new[j]
    temp = str(int(temp)+1)
    new = temp
    idx = 0
    while mid1-idx >= 0:
        N[mid2+idx] = new[mid1-idx]
        idx += 1
    for j in range(len(new)):
        N[j] = new[j]

temp = ''
for i in range(len(N)):
    temp+=N[i]
print(int(temp))