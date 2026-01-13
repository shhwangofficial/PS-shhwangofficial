import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))

ordered = sorted(range(1, N + 1))


def dfs(depth, lst, ans):
    if lst == ordered:
        for fr, end in ans:
            print(fr + 1, end)
        for _ in range(3 - len(ans)):
            print("1 1")
        exit()
    if depth == 3:
        return

    indexs = [0]
    prev_d = None
    for i in range(1, N):
        d = lst[i] - lst[i - 1]

        if d == 1:
            cur = 1
        elif d == -1:
            cur = -1
        else:
            cur = None

        # run 끊김 조건
        if cur is None or prev_d is None or cur != prev_d:
            indexs.append(i)

        prev_d = cur

    indexs.append(N)

    indexs = sorted(list(indexs))
    for i in range(len(indexs)):
        for j in range(i + 1, len(indexs)):
            fr, end = indexs[i], indexs[j]
            temp = lst[:]
            temp[fr:end] = reversed(temp[fr:end])

            dfs(depth + 1, temp, ans + [(fr, end)])


dfs(0, lst, [])
