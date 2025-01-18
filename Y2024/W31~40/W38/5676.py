def make_tree(start, end, idx_tree):
    if start == end:
        global num
        seg_tree[idx_tree] = num[start]

    else:
        mid = (start + end) // 2
        seg_tree[idx_tree] = make_tree(start, mid, 2 * idx_tree) * make_tree(mid + 1, end, 2 * idx_tree + 1)

    return seg_tree[idx_tree]


def update(start, end, idx_tree, idx, val):
    if start == end:
        seg_tree[idx_tree] = val
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(start, mid, idx_tree * 2, idx, val)
    else:
        update(mid + 1, end, idx_tree * 2 + 1, idx, val)
    seg_tree[idx_tree] = seg_tree[idx_tree * 2] * seg_tree[idx_tree * 2 + 1]


def get_val(start, end, idx_tree, fr, to):
    if start == fr and end == to:
        return seg_tree[idx_tree]

    mid = (start + end) // 2
    if mid < fr:
        return get_val(mid + 1, end, 2 * idx_tree + 1, fr, to)
    elif to <= mid:
        return get_val(start, mid, 2 * idx_tree, fr, to)
    else:
        return get_val(start, mid, 2 * idx_tree, fr, mid) * get_val(mid + 1, end, 2 * idx_tree + 1, mid + 1, to)


while True:
    try:
        N, K = map(int, input().split())
        num = list(map(int, input().split()))
        seg_tree = [0] * (4 * N)
        ans = ""
        for i in range(N):
            if num[i] > 0:
                num[i] = 1
            elif num[i] == 0:
                num[i] = 0
            elif num[i] < 0:
                num[i] = -1
        make_tree(0, N - 1, 1)
        for _ in range(K):
            comm, i, j = map(str, input().split())
            if comm == "C":
                i, val = int(i) - 1, int(j)
                if val > 0:
                    val = 1
                elif val == 0:
                    val = 0
                elif val < 0:
                    val = -1
                update(0, N - 1, 1, i, val)
            elif comm == "P":
                i, j = int(i) - 1, int(j) - 1
                got = get_val(0, N - 1, 1, i, j)
                if got > 0:
                    ans += "+"
                elif got == 0:
                    ans += "0"
                elif got < 0:
                    ans += "-"

        print(ans)

    except EOFError:
        break
