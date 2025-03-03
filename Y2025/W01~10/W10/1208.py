N, S = map(int, input().split())
nums = list(map(int, input().split()))
left = nums[: (N // 2)]
right = nums[(N // 2) :]
left_sum = []
right_sum = []

for i in range(1 << (len(left))):
    temp = 0
    for j in range(len(left) + 1):
        if i & (1 << j):
            temp += left[j]
    left_sum.append(temp)

for i in range(1 << (len(right))):
    temp = 0
    for j in range(len(right) + 1):
        if i & (1 << j):
            temp += right[j]
    right_sum.append(temp)

right_sum.sort()
before = right_sum[0]
cnt = 1
real_right_sum = []
for i in range(1, len(right_sum)):
    if right_sum[i] != before:
        real_right_sum.append((before, cnt))
        before = right_sum[i]
        cnt = 1
    else:
        cnt += 1
real_right_sum.append((before, cnt))


ans = 0
for ls in left_sum:
    s, e = 0, len(real_right_sum) - 1
    while s <= e:
        mid = (s + e) // 2
        if real_right_sum[mid][0] + ls == S:
            ans += real_right_sum[mid][1]
            break
        elif real_right_sum[mid][0] + ls < S:
            s = mid + 1
        else:
            e = mid - 1

print(ans - 1 if S == 0 else ans)
