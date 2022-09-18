MOD = 10007

def solution(n):
    dp = [[1] * 10 for _ in range( n+ 1)]
    for length in range(2,n+1):
        for digit in range(1,10):
            dp[length][digit] = dp[length][digit -1] + dp[length-1][digit]
            dp[length][digit] %= MOD

    return sum(dp[n]) % MOD

n = 2
print(solution(n))