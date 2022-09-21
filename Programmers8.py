from multiprocessing.connection import answer_challenge


def getNextNodes(i,prev,adj_list):
    nextNode = [edge for edge in prev if edge != i]
    for j in range(len(adj_list)):
        if adj_list[i][j] == True:
            nextNode.append(j)

    return nextNode

def DFS(i,sheep,wolf,prev,adj_list,info):
    global answer
    nextNode = getNextNodes(i,prev,adj_list)
    if sheep == wolf or not nextNode:
        if answer < sheep:
            answer = sheep
        return
    for node in nextNode:
        if info[node] == 0:
            DFS(node,sheep + 1,wolf,nextNode,adj_list,info)
        else:
            DFS(node,sheep,wolf + 1,nextNode,adj_list,info)

def solution(info,edges):
    global answer
    answer = 1
    adj_list = [[False] * len(info) for _ in range(len(info))]
    for x,y in edges:
        adj_list[x][y] = True
    DFS(0,1,0,[0],adj_list,info)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))