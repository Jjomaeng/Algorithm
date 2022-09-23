board = []

def validate(x,y,a,n):
    if a == 0:
        if y == 0:
            return True
        if board[x][y][1] or (x > 0 and board[x-1][y][1]):
            return True
        if y > 0 and board[x][y-1][0]:
            return True
    else :
        if y > 0 and board[x][y-1][0]:
            return True
        if x < n and y > 0 and board[x+1][y-1][0]:
            return True
        if 0 < x < n-1 and board[x-1][y][1] and board[x+1][y][1]:
            return True
    return False

def check_removable(x,y,n):
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            nx,ny = x + dx, y + dy
            if not(0 <= nx <= n and 0 <= ny <= n):
                continue
            for j in range(2):
                if board[nx][ny][j] and not validate(nx,ny,j,n):
                    return False

    return True


def solution(n,build_frame):
    global board
    board = [[[False] * 2 for _ in range(n+1)] for _ in range(n+1)]
    answer = []


    for x,y,a,b in build_frame:
        if b == 0:
            board[x][y][a] = False
            if not check_removable(x,y,n):
                board[x][y][a] = True
        else :
            if validate(x,y,a,n):
                board[x][y][a] = True
    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if board[i][j][k]:
                    answer.append([i,j,k])

    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))