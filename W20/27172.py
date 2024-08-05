import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

cards_w_idx = {card: idx for idx, card in enumerate(cards)}
max_card = max(cards)

res = [0] * n

for i in range(n):
    cur_card = cards[i]
    for j in range(cur_card * 2, max_card + 1, cur_card):
        if j in cards_w_idx:
            res[i] += 1
            res[cards_w_idx[j]] -= 1

print(*res)


# import sys
# input = sys.stdin.readline

# N = int(input())
# x = list(map(int, input().rstrip().split()))
# S = set(x)
# M = max(x)
# sieve = [0 for _ in range(M+1)]
# for i in x:
#     if i == M: continue
#     for j in range(2*i, M+1, i):
#         if j in S:
#             sieve[i] += 1
#             sieve[j] -= 1
# for i in x:
#     print(sieve[i], end = ' ')
