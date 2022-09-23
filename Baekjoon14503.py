def solution(n,m,r,c,d,board):
    answer = 0

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while True:
        if board[r][c] == 0:
            answer += 1
            board[r][c] = 2

        for _ in range(4) :
            d = (d + 3) % 4
            nx = r + dx[d]
            ny = c + dy[d]
            if (board[nx][ny] == 0):
                r = nx
                c = ny
                break
        else :
            nd = (d + 2) % 4
            nx = r + dx[nd]
            ny = c + dy[nd]
            if board[nx][ny] == 1:
                break
                
            r = nx
            c = ny
    return answer
        
        