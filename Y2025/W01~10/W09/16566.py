N, M, K = map(int, input().split())
blue_cards = sorted(list(map(int, input().split())))
red_cards = list(map(int, input().split()))
group = [i for i in range(M)]


def binary_search(red):
    s, e = 0, M - 1
    while s <= e:
        mid = (s + e) // 2
        if blue_cards[mid] > red:
            ret = mid
            e = mid - 1
        else:
            s = mid + 1
    return ret


def find(idx):
    while idx != group[idx]:
        idx = group[idx]
    return idx


for red in red_cards:
    idx = binary_search(red)
    real_index = find(idx)
    print(blue_cards[real_index])
    group[real_index] += 1
