import queue


def solution(m,n,picture):
    number_of_area = 0
    max_size_of_one_area = 0

    dx = [0,0,-1,+1]
    dy = [-1,1,0,0]

    que = queue.Queue()

    for i in range(m):
        for j in range(n):
            if picture[i][j] == 0 : continue
            else :
                number_of_area += 1
                count = 0
                que.put((i,j))
                color = picture[i][j]
                picture[i][j] = 0

                while que.qsize() > 0:
                    count += 1
                    x,y = que.get()
                    for k in range(4):
                        if 0 <=x+dx[k] < m and 0<=y+dy[k] < n and picture[x+dx[k]][y+dy[k]] == color :
                            que.put((x+dx[k],y+dy[k]))
                            picture[x+dx[k]][y+dy[k]] = 0

                max_size_of_one_area = max(max_size_of_one_area,count)

    return [number_of_area,max_size_of_one_area]

m,n = 6,4
picture = [[1,1,1,0],[1,2,2,0],[1,0,0,1],[0,0,0,1],[0,0,0,3],[0,0,0,3]]

print(solution(m,n,picture))