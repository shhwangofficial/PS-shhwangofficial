def rotate_plane(plane, dir):
    new_plane = [[0] * 3 for _ in range(3)]
    if dir == "+":
        for r in range(3):
            for c in range(3):
                new_plane[c][2 - r] = plane[r][c]
    else:
        for r in range(3):
            for c in range(3):
                new_plane[2 - c][r] = plane[r][c]
    return new_plane


def rotate_surround_main(plane, dir):
    up_row = main[plane - 1][-1]
    down_row = main[(plane + 1) % 4][0]
    lst = []
    for i in range(3):
        lst.append(up_row[i])
    for i in range(3):
        lst.append(right[i][0])
    for i in range(3 - 1, -1, -1):
        lst.append(down_row[i])
    for i in range(3 - 1, -1, -1):
        lst.append(left[i][2])

    if dir == "-":
        add = 3
    else:
        add = -3

    for i in range(3):
        main[plane - 1][-1][i] = lst[(i + add) % 12]
    for i in range(3, 3 + 3):
        right[i - 3][0] = lst[(i + add) % 12]
    for i in range(6, 6 + 3):
        main[(plane + 1) % 4][0][2 - (i - 6)] = lst[(i + add) % 12]
    for i in range(9, 9 + 3):
        left[2 - (i - 9)][2] = lst[(i + add) % 12]


def vertical(rotated, dir):
    lst = []
    if rotated == "left":
        col = 0
    else:
        col = 2

    if (rotated == "left" and dir == "-") or (rotated == "right" and dir == "+"):
        add = 3
    else:
        add = -3

    for plane in range(4):
        for row in range(3):
            lst.append(main[plane][row][col])
    for plane in range(4):
        for row in range(3):
            main[plane][row][col] = lst[(plane * 3 + row + add) % 12]


T = int(input())
for _ in range(T):
    n = int(input())
    command = list(map(str, input().split()))
    main = [
        [
            ["w", "w", "w"],
            ["w", "w", "w"],
            ["w", "w", "w"],
        ],
        [
            ["r", "r", "r"],
            ["r", "r", "r"],
            ["r", "r", "r"],
        ],
        [
            ["y", "y", "y"],
            ["y", "y", "y"],
            ["y", "y", "y"],
        ],
        [
            ["o", "o", "o"],
            ["o", "o", "o"],
            ["o", "o", "o"],
        ],
    ]

    left = [
        ["g", "g", "g"],
        ["g", "g", "g"],
        ["g", "g", "g"],
    ]
    right = [
        ["b", "b", "b"],
        ["b", "b", "b"],
        ["b", "b", "b"],
    ]

    for comm in command:
        if comm[0] == "L" or comm[0] == "R":
            if comm[0] == "L":
                left = rotate_plane(left, comm[1])
                vertical("left", comm[1])
            else:
                right = rotate_plane(right, comm[1])
                vertical("right", comm[1])
        else:
            if comm[0] == "U":
                left = rotate_plane(left, "+")
                right = rotate_plane(right, "-")
                main[0] = rotate_plane(main[0], comm[1])
                rotate_surround_main(0, comm[1])
                left = rotate_plane(left, "-")
                right = rotate_plane(right, "+")
            elif comm[0] == "F":
                main[1] = rotate_plane(main[1], comm[1])
                rotate_surround_main(1, comm[1])
            elif comm[0] == "D":
                left = rotate_plane(left, "-")
                right = rotate_plane(right, "+")
                main[2] = rotate_plane(main[2], comm[1])
                rotate_surround_main(2, comm[1])
                left = rotate_plane(left, "+")
                right = rotate_plane(right, "-")
            elif comm[0] == "B":
                left = rotate_plane(left, "-")
                right = rotate_plane(right, "+")
                left = rotate_plane(left, "-")
                right = rotate_plane(right, "+")
                main[3] = rotate_plane(main[3], comm[1])
                rotate_surround_main(3, comm[1])
                left = rotate_plane(left, "+")
                right = rotate_plane(right, "-")
                left = rotate_plane(left, "+")
                right = rotate_plane(right, "-")

    for row in main[0]:
        print("".join(row))
