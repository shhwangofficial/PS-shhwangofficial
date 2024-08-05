import sys


def manber_myers(s):
    n = len(s)
    suffix_array = list(range(n))
    rank = [ord(c) for c in s]
    k = 1

    while k < n:
        key = [(rank[i], rank[i + k] if i + k < n else -1) for i in range(n)]
        suffix_array.sort(key=lambda x: (key[x]))

        temp_rank = [0] * n
        for i in range(1, n):
            temp_rank[suffix_array[i]] = temp_rank[suffix_array[i - 1]]
            if key[suffix_array[i]] > key[suffix_array[i - 1]]:
                temp_rank[suffix_array[i]] += 1
        rank = temp_rank
        k *= 2

    return suffix_array


s = sys.stdin.readline().rstrip()
suffix_array = manber_myers(s)
for i in range(len(suffix_array)):
    print(suffix_array[i])
