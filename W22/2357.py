import sys
from math import log2, ceil
N, M = map(int,sys.stdin.readline().split())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
H = ceil(log2(N))
tree = [0] * (2**(H+1))
def making_tree(start, end, idx):
    if start == end:
        tree[idx] = [num[start], num[start]]
        return tree[idx]
    
    mid = (start + end) // 2
    left_tree = making_tree(start, mid, idx*2)
    right_tree = making_tree(mid+1,end, idx*2+1)
    tree[idx] = [min(left_tree[0], right_tree[0]), max(left_tree[1], right_tree[1])]
    return tree[idx]


making_tree(0, N-1, 1)
def query(start, end, left, right, idx):
    if start == left and end == right:
        return tree[idx]
    
    mid = (start+ end)//2
    if right <= mid:
        return query(start, mid, left, right, idx*2)
    elif mid+1 <= left:
        return query(mid+1, end, left, right, idx*2+1)
    else:
        left_tree = query(start, mid, left, mid, idx*2)
        right_tree = query(mid+1, end, mid+1, right, idx*2+1)
        return [min(left_tree[0], right_tree[0]), max(left_tree[1], right_tree[1])]
        




for _ in range(M):
    left, right = map(int,sys.stdin.readline().split())
    print(*query(0, N-1, left-1, right-1, 1))