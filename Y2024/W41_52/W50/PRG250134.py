# https://school.programmers.co.kr/learn/courses/30/lessons/250134

answer = 999


def solution(maze):
    row = len(maze)
    col = len(maze[0])
    visited_red = [[0] * col for _ in range(row)]
    visited_blue = [[0] * col for _ in range(row)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def dfs(visited_red, visited_blue, turn, redx, redy, bluex, bluey):
        global answer
        if turn > answer:  # 킥이다.
            return

        if maze[redx][redy] == 3 and maze[bluex][bluey] == 4:
            answer = min(answer, turn)
            return

        visited_red[redx][redy] = 1
        visited_blue[bluex][bluey] = 2

        for i in range(4):
            if maze[redx][redy] == 3:
                nredx, nredy = redx, redy
            else:
                nredx, nredy = redx + dx[i], redy + dy[i]
            if (
                0 <= nredx < row
                and 0 <= nredy < col
                and (visited_red[nredx][nredy] != 1 or maze[redx][redy] == 3)
                and maze[nredx][nredy] != 5
            ):
                for j in range(4):
                    if maze[bluex][bluey] == 4:
                        nbluex, nbluey = bluex, bluey
                    else:
                        nbluex, nbluey = bluex + dx[j], bluey + dy[j]
                    if (
                        0 <= nbluex < row
                        and 0 <= nbluey < col
                        and (visited_blue[nbluex][nbluey] != 2 or maze[bluex][bluey] == 4)
                        and maze[nbluex][nbluey] != 5
                    ):
                        if (not (nredx == nbluex and nredy == nbluey)) and (
                            not ((nredx == bluex and nredy == bluey) and (nbluex == redx and nbluey == redy))
                        ):
                            dfs(
                                visited_red,
                                visited_blue,
                                turn + 1,
                                nredx,
                                nredy,
                                nbluex,
                                nbluey,
                            )

        visited_red[redx][redy] = 0
        visited_blue[bluex][bluey] = 0

    for r in range(row):
        for c in range(col):
            if maze[r][c] == 1:
                redx, redy = r, c
            if maze[r][c] == 2:
                bluex, bluey = r, c

    dfs(visited_red, visited_blue, 0, redx, redy, bluex, bluey)

    return answer if answer != 999 else 0
