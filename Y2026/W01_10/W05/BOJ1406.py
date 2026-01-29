from collections import deque
import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

word = input()
M = int(input())
cursor_left = deque(word)
cursor_right = deque()
for _ in range(M):
    command = input()
    if command[0] == "L":
        if cursor_left:
            cursor_right.appendleft(cursor_left.pop())
    elif command[0] == "D":
        if cursor_right:
            cursor_left.append(cursor_right.popleft())
    elif command[0] == "B":
        if cursor_left:
            cursor_left.pop()
    elif command[0] == "P":
        cursor_left.append(command[2])

print("".join(cursor_left + cursor_right))
