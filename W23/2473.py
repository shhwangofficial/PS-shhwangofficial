import sys
N = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()

left = 0
right = N-1
mid = 1

ans_list = [liq[left], liq[mid], liq[right]]
ans = sum(ans_list)

while left != right -1:
    SUM = liq[left] + liq[mid] + liq[right]

    if SUM == 0:
        ans_list = [liq[left], liq[mid], liq[right]]
        break

    if abs(SUM) < abs(ans):
        ans_list = [liq[left], liq[mid], liq[right]]
        ans = SUM

    if SUM < 0:
        mid += 1
    elif SUM > 0:
        right -= 1

    if mid == right:
        left += 1
        mid = left + 1
        right = N-1

print(*ans_list)

