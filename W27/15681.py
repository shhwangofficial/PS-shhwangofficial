import sys
sys.setrecursionlimit(10**8)
N, R, Q = map(int,sys.stdin.readline().split())
graph= [[] for i in range(N+1)]
for i in range(N-1):
    U, V = map(int,sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)

children= [[] for i in range(N+1)]

def maketree(current, parent):
    for node in graph[current]:
        if node != parent:
            children[current].append(node)
            maketree(node, current)

def countSubtreeNodes(current):
    size[current] = 1
    for node in children[current]:
        countSubtreeNodes(node)
        size[current] += size[node]



size = [0] * (N+1)
root = R
maketree(root, -1)
countSubtreeNodes(root)
for i in range(Q):
    node = int(sys.stdin.readline())
    print(size[node])