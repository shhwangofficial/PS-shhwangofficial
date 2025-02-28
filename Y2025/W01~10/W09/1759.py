L, C = map(int, input().split())
characters = list(map(str, input().split()))

characters.sort()


def backtrack(N, string, vowel, cons):
    if len(string) >= L:
        if vowel >= 1 and cons >= 2:
            print(string)
        return
    for i in range(N + 1, C):
        if characters[i] in ["a", "e", "i", "o", "u"]:
            backtrack(i, string + characters[i], vowel + 1, cons)
        else:
            backtrack(i, string + characters[i], vowel, cons + 1)


backtrack(-1, "", 0, 0)
