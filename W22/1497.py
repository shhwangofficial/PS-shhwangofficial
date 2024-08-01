import sys
from itertools import combinations
N, M = map(int,sys.stdin.readline().split())
songs_of_guitars = set()
for i in range(N):
    guitar, songs = sys.stdin.readline().split()
    String = ''
    for j in range(M):
        if songs[j] == "Y":
            String += "1"
        else:
            String += "0"
    songs_of_guitars.add(int(String, 2))

if songs_of_guitars == {0}:
    print(-1)
    exit(0)

max_cnt = 0
min_guitars = 0
for i in range(1, len(songs_of_guitars)+1):
    for j in combinations(songs_of_guitars, i):
        S = 0
        for k in j:
            S |= k
        cnt = 0
        for k in range(M):
            if (S & 1<<k) > 0:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            min_guitars = i

print(min_guitars)

    

