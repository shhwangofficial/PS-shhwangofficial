import sys
row, col, num_shark = map(int,sys.stdin.readline().split())
board = [[0]*col for i in range(row)]
sharks = []
for i in range(num_shark):
    r,c,s,d,z = map(int,sys.stdin.readline().split())
    r -= 1
    c -= 1
    board[r][c] = [s, d, z, i]
    sharks.append([r,c,s,d,z])
direction = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, 1],
    4: [0, -1],
}
caught = 0
for i in range(col):
    cr = -1
    cc = -1
    for j in range(row):
        if board[j][i] != 0:
            caught += board[j][i][2]
            cr, cc = j, i
            break
    board = [[0]*col for i in range(row)]    
    for j in range(len(sharks)):
        if sharks[j] != 0:
            r = sharks[j][0]
            c = sharks[j][1]
            if r == cr and c == cc:
                sharks[j] = 0
                continue
            r, c = r + sharks[j][2]*direction[sharks[j][3]][0], c + sharks[j][2]*direction[sharks[j][3]][1]
            # r,c를 수정
            if r >= row:
                rem = ((r-1) % (row-1))+1
                val = (r-1) // (row-1)
                if val % 2 == 1:
                    # 방향 반대
                    sharks[j][3] = (sharks[j][3])%2+1
                    r = row-1 + (-1)*(rem)
                else:
                    r = rem
            elif r < 0:
                if (((-1*r) -1) // (row-1)) % 2 == 0:
                    r = (((-1*r) -1) % (row-1)) + 1
                    sharks[j][3] = (sharks[j][3])%2+1
                else:
                    r = (row-1-((-1*r) % (row-1))) %(row-1)
                    
            if c >= col:
                rem = ((c-1) % (col-1))+1
                val = (c-1) // (col-1)
                if val % 2 == 1:
                    # 방향 반대
                    sharks[j][3] = (sharks[j][3]-3+1)%2+3
                    c = col-1 + (-1)*(rem)
                else:
                    c = rem

            elif c < 0:
                if (((-1*c) -1) // (col-1)) % 2 == 0:
                    c = (((-1*c) -1) % (col-1)) + 1
                    sharks[j][3] = (sharks[j][3]-3+1)%2+3
                else:
                    c = (col-1-((-1*c) % (col-1))) %(col-1)
                
            if board[r][c] == 0:
                board[r][c] = [sharks[j][2], sharks[j][3], sharks[j][4], j]
                sharks[j][0], sharks[j][1] = r, c    
            else:
                if board[r][c][2] < sharks[j][4]:
                    sharks[board[r][c][3]] = 0
                    board[r][c] = [sharks[j][2], sharks[j][3], sharks[j][4], j]
                    sharks[j][0], sharks[j][1] = r, c
                else:
                    sharks[j] = 0
            
print(caught)