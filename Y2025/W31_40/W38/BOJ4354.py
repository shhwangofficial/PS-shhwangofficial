import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

while True:
    word = input()
    if word == ".":
        break

    length = len(word)
    if length == 1:
        print(1)
        continue

    i, j = 0, 1
    suffix = [0] * length
    while j < length:
        if word[i] == word[j]:
            suffix[j] = i + 1
            if j == length - 1:
                break
            i += 1
            j += 1
        else:
            if i == 0:
                j += 1
            else:
                i = 0

    if suffix[-1] < length / 2:
        print(1)
        continue

    now = suffix[-1]
    err = 0
    for i in range(length - 1, -1, -1):
        if now != suffix[i]:
            print(1)
            err = 1
            break
        now -= 1
        if now == 0:
            ans = i - 1
            break

    if err or length % (ans + 1):
        print(1)
    else:
        print(length // (ans + 1))
