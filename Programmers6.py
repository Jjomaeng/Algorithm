from copy import deepcopy

max_diff = 0
answer = []

def calcDiff(apeach,ryan):
    enemyScore,myScore = 0,0
    for i in range(11):
        if (apeach[i] , ryan[i]) == (0,0):
            continue
        if apeach[i] >= ryan[i]:
            enemyScore += (10 - i)
        else :
            myScore += (10 - i)

    return myScore - enemyScore

def dfs(apeach,ryan,n,i):
   
    global answer,max_diff
    if i == 11:
        if n != 0:
            ryan[10] = n
        score_diff = calcDiff(apeach,ryan)
        if score_diff <= 0:
            return
        result = deepcopy(ryan)
        if score_diff > max_diff :
            max_diff = score_diff
            answer = [result]
            return
        if score_diff == max_diff:
            answer.append(result)
        return

    if apeach[i] < n :
        ryan.append(apeach[i] + 1)
        dfs(apeach,ryan,n-apeach[i]-1,i + 1)
        ryan.pop()
     


    ryan.append(0)
    dfs(apeach,ryan,n,i + 1)
    ryan.pop()


def solution(n,info):
    global answer,max_diff
    dfs(info,[],n,0)
    if answer == []:
        return [-1]
    answer.sort(key = lambda x : x [::-1],reverse= True)
    return answer[0]

solution(5,[2,1,1,1,0,0,0,0,0,0,0])