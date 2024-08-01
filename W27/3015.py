import sys
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))

stack = []
cnt = 0
for i in nums:
    if not stack:
        stack.append([i,1])
    elif stack[-1][0] > i:
        stack.append([i,1])
        cnt += 1
    elif stack[-1][0] == i:
        cnt += stack[-1][1]
        if len(stack) > 1:
            cnt += 1
        stack[-1][1] += 1
    else:
        while stack and stack[-1][0] < i:
            cnt += stack.pop()[1]
        if not stack:
            stack.append([i,1])
        elif stack[-1][0] > i:
            stack.append([i,1])
            cnt += 1
        elif stack[-1][0] == i:
            cnt += stack[-1][1]
            if len(stack) > 1:
                cnt += 1
            stack[-1][1] += 1


print(cnt)