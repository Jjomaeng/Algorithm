from re import L
import sys

INF = 1e7

def fillGraph(n,fares):
    graph = [[INF] * (n + 1) for _ in range( n + 1)]

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

                graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])

def solution(n,s,a,b,fares,lay) :
    answer = INF
    graph = fillGraph(n,fares)

    floydWarshall(graph,n)


    for i in range(1,n+1):
        answer = min(answer,graph[s][lay] + graph[lay][i] + graph[i][a] + graph[i][b])
    return answer

n = 7
s = 3
a = 4
b = 1
c = 2
fares = [(1,2,6),(1,4,13),(2,7,5),(7,5,9),(4,5,10),(4,6,4),(6,3,1),(5,3,21),(2,3,3)]

print(solution(n,s,a,b,fares,c))