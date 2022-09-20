from re import L


INF = 1e7

def fillGraph(n,fares):
    graph = [[INF] * (n+1) for _ in range(n + 1)]
    for i in range(1,n+1):
        graph[i][i] = 0

    for u,v,w in fares:
        graph[u][v] = w
        graph[v][u] = w

    return graph
def floydWarshall(graph,n):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][i])

def solution(n,s,a,b,fares):
    answer  = INF

    graph = fillGraph(n,fares)

    floydWarshall(graph,n)

    for i in range(1,n+1):
        answer = min(answer,graph[s][i]+ graph[i][a]+ graph[i][b])