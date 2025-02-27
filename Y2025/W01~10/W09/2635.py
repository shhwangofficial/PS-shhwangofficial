N = int(input())
max_ = 0
result = []
for i in range(N):
    stack = [N, N - i]
    while True:
        if stack[-1] < 0:
            stack.pop()
            break
        else:
            stack.append(stack[-2] - stack[-1])
    if max_ < len(stack):
        result = stack[:]
        max_ = len(stack)

print(max_)
print(*result)
