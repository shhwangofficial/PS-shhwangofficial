a, b, c = map(int, input().split())
cut = 0
if max(a, b, c) > 3:
    cut = (min(a, b, c) - 1) // 2
print(cut)
