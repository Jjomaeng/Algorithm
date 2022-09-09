def dfs(v,visited,x,y,sum,cnt):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    nx = 0
    ny = 0

    if(cnt == 5):
        if(visited[sum] == False):
            visited[sum] = True

        return 

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx >= 0 and ny >= 0 and nx < 5 and ny < 5):
            dfs(v,visited,nx,ny,sum * 10 + v[nx][ny],cnt + 1)
    return 

def solution(v):
    answer = 0
    visited = [0] * 1000000

    for i in range(5):
        for j in range(5):
            dfs(v,visited,i,j,v[i][j],0)

    for i in range(1000000):
        if (visited[i] == 1) : answer += 1

    return answer

input = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,2,1],[1,1,1,1,1]]

print(solution(input))