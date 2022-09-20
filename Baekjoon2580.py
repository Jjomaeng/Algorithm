import sys
from turtle import back
sys.setrecursionlimit(10 ** 8)

row = [[0]*10 for _ in range(9)]
col = [[0]*10 for _ in range(9)]
area = [[0]*10 for _ in range(9)]
blank_cord = []

def find_area(x,y):
    return 3 * (x //3) + (y//3)

def backtracking(k,N,answer):
    if k == N : return True
    i,j = blank_cord[k]
    a = find_area(i,j)

    for x in range(1,10):
        if row[i][x] == 0 and col[j][x] == 0 and area[a][x] == 0:
            row[i][x] = 1
            col[j][x] = 1
            area[a][x] = 1

            answer[i][j] = x
            if backtracking(k+1,N,answer):
                return True
            
            row[i][x] = 0
            col[j][x] = 0
            area[a][x] = 0

    return False

def solution(sudoku):
    answer = [[0]*9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0: blank_cord.append((i,j))
            else:
                row[i][sudoku[i][j]] = 1
                col[j][sudoku[i][j]] = 1
                area[find_area(i,j)][sudoku[i][j]] = 1
                answer[i][j] = sudoku[i][j]
    backtracking(0,len(blank_cord),answer)
    return answer

sudoku = [[0,3,5,4,6,9,2,7,8],
          [7,8,2,1,0,5,6,0,9],
          [0,6,0,2,7,8,1,3,5],
          [3,2,1,0,4,6,8,9,7],
          [8,0,4,9,1,3,5,0,6],
          [5,9,6,8,2,0,4,1,3],
          [9,1,7,6,5,2,0,8,0], 
          [6,0,3,7,0,1,9,5,2],
          [2,5,8,3,9,4,7,6,0]]

print(solution(sudoku))