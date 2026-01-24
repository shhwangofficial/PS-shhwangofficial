import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numerals = input()
myway = []


def dfs(carry=""):
    if len(carry) == N // 2:
        myway.append(carry)
        return
    if not carry:
        dfs("0")
        dfs("1")
        return
    if carry[-1] == "0":
        dfs(carry + "1")
    dfs(carry + "0")


def calc(l, o, r):
    l, r = int(l), int(r)
    if o == "+":
        return l + r
    if o == "*":
        return l * r
    if o == "-":
        return l - r


dfs()
if N == 1:
    print(numerals[0])
    exit()
ans = -float("inf")
for way in myway:
    new = []
    for i in range(len(way)):
        if way[i] == "0":
            if i == 0 or way[i - 1] == "0":
                new.append(int(numerals[2 * i]))
                new.append(numerals[2 * i + 1])
            elif way[i - 1] == "1":
                new.append(numerals[2 * i + 1])
            if i == len(way) - 1:
                new.append(int(numerals[2 * i + 2]))
        elif way[i] == "1":
            new.append(calc(numerals[2 * i], numerals[2 * i + 1], numerals[2 * i + 2]))

    val = new[0]
    for i in range(1, len(new) - 1, 2):
        val = calc(val, new[i], new[i + 1])
    ans = max(ans, val)

print(ans)
