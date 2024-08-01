import sys
N = int(sys.stdin.readline())

def combination(n, r):
    val = 1
    if n-r < r:
        r = n-r
    for i in range(n, n-r, -1):
        val *= i
    for i in range(r,0,-1):
        val //= i
    return int(val)


def more_than_one(total_card, picked_card):
    if picked_card < 4:
        return 0
    val = 0
    for i in range(1, picked_card//4+1):
        val += combination(total_card//4, i) * (combination(total_card-4*i, picked_card-4*i)-(more_than_one(total_card-4*i, picked_card-4*i)))
        val %= 10007
    return val

print(more_than_one(52, N))