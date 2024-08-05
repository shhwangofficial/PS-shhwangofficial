import sys

N = int(sys.stdin.readline())

dict_ = {}

for i in range(N):
    query = tuple(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        a = query[1]
        set_query = {a, a + 1, a + 2, a + 3}
        max_ = 0
        for j in set_query:
            max_ = max(max_, dict_.get(j, 0))
        for j in set_query:
            dict_[i] = max_ + 1

    elif query[0] == 2:
        dict_[query[1]] = dict_.get(query[1], 0) + 4

    else:
        print(dict_.get(query[1], 0))
