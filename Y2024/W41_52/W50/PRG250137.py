def solution(bandage, health, attacks):
    time = 0
    attack_i = 0
    heal_time = 0
    hp = health
    answer = 0
    while hp:
        if attacks[attack_i][0] == time:
            hp -= attacks[attack_i][1]
            attack_i += 1
            heal_time = 0
            if attack_i == len(attacks):
                if hp <= 0:
                    return -1
                break
        else:
            hp = min(health, hp + bandage[1])
            heal_time += 1
            if heal_time == bandage[0]:
                hp = min(health, hp + bandage[2])
                heal_time = 0

        if hp <= 0:
            return -1

        time += 1

    answer = hp
    return answer
