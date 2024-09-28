"""
dp임을 알았어도,
저장 되는 주체가 누구인지에 따라 달라진다
현 문제 풀이는 '각 스티커가 선택 된다면'의 가정을 해서 dp에 더해갔고,
내 기존 풀이는 '다음 단계의 최선이 무엇일까' 만 생각했음.
"""

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [[0, 0] + list(map(int, input().split())) for _ in range(2)]

    DP = [[0] * (N + 2) for _ in range(2)]

    for i in range(2, N + 2):
        DP[0][i] = max(DP[1][i - 2], DP[1][i - 1]) + arr[0][i]
        DP[1][i] = max(DP[0][i - 2], DP[0][i - 1]) + arr[1][i]

    print(max(DP[0][-1], DP[1][-1]))
