import sys
from collections import deque

def playGame(n,board,cmd):
    dr = [0,-1,0,1]
    dc = [1,0,-1,0]
    t = 0
    head = 0
    snake = deque()
    snake.appendleft([0,0])
    board[0][0] = 1

    while(True):
        t += 1
        nr = snake[0][0] + dr[head]
        nc = snake[0][1] + dc[head]

        if(nr < 0 or nr >=n or nc < 0 or nc >= n or board[nr][nc] == 1 ) : break

        if (board[nr][nr] != 2) :
            x,y = snake.pop()
            board[x][y] = 0

        snake.appendleft([nr,nc])
        board[nr][nc] = 1

        if (cmd.get(t) == 'L') : head = (head + 1) % 4
        elif (cmd.get(t) == 'D') : head = (head +3) % 4

    return t

def solution(n,k,l,apple,rotation):
    answer = 0
    board = [[0] * n for _ in range(n)]

    for i ,j in apple:
        board[i-1][j-1] = 2
    
    cmd = dict(rotation)
    answer = playGame(n,board,cmd)

    return answer

N = 6
K = 3
apple = [(3,4),(2,5),(5,3)]
L = 3
rotation = [(3,'D'),(15,'L'),(17,"D")]

print(solution(N,K,L,apple,rotation))