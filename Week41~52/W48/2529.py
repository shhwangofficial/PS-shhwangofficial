import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip().split(" ")

visited = [0] * 10
min_ = ""
max_ = ""


def backtrack(visited, ans, i):
    if i == N + 1:
        global min_
        if min_ == "":
            min_ = ans
        global max_
        max_ = ans
        return
    if i == 0:
        range_ = range(10)
    elif string[i - 1] == "<":
        range_ = range(int(ans[-1]) + 1, 10)
    else:
        range_ = range(0, int(ans[-1]))

    for j in range_:
        if visited[j] == 0:
            visited[j] = 1
            backtrack(visited, ans + str(j), i + 1)
            visited[j] = 0


backtrack(visited, "", 0)
print(max_)
print(min_)
