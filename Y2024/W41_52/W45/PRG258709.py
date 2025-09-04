# 주사위 고르기
from itertools import combinations


def solution(dice):
    def backtrack(lst, n, dice_lst):
        if len(lst) == n:
            score = 0
            for i in range(n):
                score += dice[dice_lst[i]][lst[i]]

            return [score]

        ret = []
        for i in range(6):
            for j in backtrack(lst + [i], n, dice_lst):
                ret.append(j)

        return ret

    answer = []
    max_win = 0
    n = len(dice) // 2
    for comb in combinations(range(len(dice)), n):
        A_dices = list(comb)
        B_dices = list(set(range(len(dice))) - set(comb))
        A_scores = sorted(backtrack([], n, A_dices))
        B_scores = sorted(backtrack([], n, B_dices))
        temp = 0
        found = -1
        prev = -1
        for A_score in A_scores:
            if prev == A_score:
                temp += found + 1
                continue
            s, e = max(0, found), len(B_scores) - 1

            while s <= e:
                mid = (s + e) // 2
                if B_scores[mid] < A_score:
                    found = mid
                    s = mid + 1
                else:
                    e = mid - 1
            temp += found + 1
            prev = A_score

        if temp > max_win:
            max_win = temp
            answer = A_dices

    for i in range(len(answer)):
        answer[i] += 1
    return answer
