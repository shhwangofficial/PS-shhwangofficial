import sys

N = int(sys.stdin.readline())
arch_list = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    arch_list.append([x - r, 1])  # 1 = (, 0 = )
    arch_list.append([x + r, 0])

arch_list.sort(key=lambda x: (x[0], x[1]))

area = 1
stack_layer = []

for [position, type_] in arch_list:
    if type_ == 1:  # (
        if stack_layer and position != prev:  # 끊는 ( 일 경우
            stack_layer[-1] = 1  # 해당 레이어는 끊겼음을 표시
        stack_layer.append(0)
    else:  # )
        area += 1
        if (
            stack_layer.pop() == 0 and position == prev
        ):  # 끊기지 않고 온전히 왔다면 area 하나 더
            area += 1
    prev = position

print(area)
