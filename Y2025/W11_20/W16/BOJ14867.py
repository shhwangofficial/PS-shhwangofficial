import sys

file_path = 0 if sys.platform == "linux" else "python_input.txt"
sys.stdin = open(file_path, "r")
input = lambda: sys.stdin.readline().rstrip()

from collections import deque, defaultdict

alimit, blimit, agoal, bgoal = map(int, input().split())
visited = defaultdict(int)
visited[(0, 0)] = 0
queue = deque([(0, 0, 0)])
ans = -1


def atob(a, b):
    bgap = blimit - b
    na = a - min(bgap, a)
    nb = b + min(bgap, a)
    if visited[(na, nb)] == 0:
        visited[(na, nb)] = 1
        queue.append((na, nb, step + 1))


def btoa(a, b):
    agap = alimit - a
    na = a + min(agap, b)
    nb = b - min(agap, b)
    if visited[(na, nb)] == 0:
        visited[(na, nb)] = 1
        queue.append((na, nb, step + 1))


def empty(a, b, what):
    if what == "a":
        if a == 0:
            return
        na = 0
        if visited[(na, b)] == 0:
            visited[(na, b)] = 1
            queue.append((na, b, step + 1))
    elif what == "b":
        if b == 0:
            return
        nb = 0
        if visited[(a, nb)] == 0:
            visited[(a, nb)] = 1
            queue.append((a, nb, step + 1))


def fill(a, b, what):
    if what == "a":
        na = alimit
        if visited[(na, b)] == 0:
            visited[(na, b)] = 1
            queue.append((na, b, step + 1))
    elif what == "b":
        nb = blimit
        if visited[(a, nb)] == 0:
            visited[(a, nb)] = 1
            queue.append((a, nb, step + 1))


while queue:
    a, b, step = queue.popleft()
    if a == agoal and b == bgoal:
        ans = step
        break
    if a == alimit:
        atob(a, b)
    elif b == blimit:
        btoa(a, b)
    else:
        atob(a, b)
        btoa(a, b)
    empty(a, b, "a")
    empty(a, b, "b")
    fill(a, b, "a")
    fill(a, b, "b")

print(ans)
