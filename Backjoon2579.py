import numpy as np

def solution(n,score):
    answer = 0
    dp = [0] * (301)
    dp[1] = score[1]
    dp[2] = score[1] + score[2]

    for i in range(3,n+1):
        dp[i] = max(dp[i-3] + score[i-1],dp[i-2]) + score[i]

    answer = dp[n]
    return answer
          

n = 6
s = [0,5,5,20,10,15,20]

print(solution(n,s))

