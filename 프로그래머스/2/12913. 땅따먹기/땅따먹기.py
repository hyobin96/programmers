def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    for j in range(4):
        dp[0][j] = land[0][j]
    
    for i in range(n - 1):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + land[i + 1][k])
    
    
    answer = max(dp[n - 1])

    return answer