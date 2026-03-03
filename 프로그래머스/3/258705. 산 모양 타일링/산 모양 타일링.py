def solution(n, tops):
    tops = [0] + tops
    dp = [0] * (n * 2 + 2)
    dp[0], dp[1] = 1, 1
    mod = 10_007
    
    for i in range(2, n * 2 + 2):
        if i % 2 == 0 and tops[i // 2]:
            dp[i] = (dp[i - 2] + dp[i - 1] * 2) % mod
            continue
        dp[i] = (dp[i - 2] + dp[i - 1]) % mod
                
    answer = dp[n * 2 + 1] % mod
    return answer