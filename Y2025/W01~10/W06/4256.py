import sys

T = int(sys.stdin.readline())


def find(pre_idx, lst):
    global ret
    if len(lst) == 1:
        ret.append(lst[0])
        return

    for i in range(len(lst)):
        if lst[i] == preorder[pre_idx]:
            find(pre_idx + 1, lst[:i])
            find(pre_idx + i + 1, lst[i + 1 :])
            ret.append(lst[i])
            break
    return


for _ in range(T):
    n = int(sys.stdin.readline())

    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))

    ret = []
    find(0, inorder)
    print(*ret)
