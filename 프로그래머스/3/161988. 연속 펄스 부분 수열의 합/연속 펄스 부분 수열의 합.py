def solution(sequence):
    n = len(sequence)
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = -sequence[0]
    dp[1][0] = sequence[0]
    
    for i in range(1, n):
        dp[0][i] = max(-sequence[i], dp[1][i - 1] - sequence[i])
        dp[1][i] = max(sequence[i], dp[0][i - 1] + sequence[i])
        
    
    answer = max(max(dp[0]), max(dp[1]))
    return answer