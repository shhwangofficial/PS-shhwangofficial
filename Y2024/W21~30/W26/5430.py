import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    cmds = sys.stdin.readline().strip()
    len_l = int(sys.stdin.readline())
    list1 = sys.stdin.readline().strip()
    if list1 == "[]":
        list1 = []
    else:
        list1 = deque(list1[1:-1].split(","))
    now = True
    for cmd in cmds:
        if cmd == "R":
            now = not now
        elif cmd == "D":
            if len(list1) == 0:
                print("error")
                break
            else:
                if now:
                    list1.popleft()
                else:
                    list1.pop()
    else:
        print("[", end="")
        while list1:
            if len(list1) == 1:
                if now:
                    print(list1.popleft(), end="")
                else:
                    print(list1.pop(), end="")
            else:
                if now:
                    print(list1.popleft(), end=",")
                else:
                    print(list1.pop(), end=",")
        print("]")
