def solution(players, callings):
    dic = {}
    for i, player in enumerate(players):
        dic[player] = i
    for call in callings:
        now = dic[call]
        dic[call] -= 1
        temp = players[now - 1]
        dic[temp] += 1
        players[now - 1] = call
        players[now] = temp
    answer = players[:]
    return answer
