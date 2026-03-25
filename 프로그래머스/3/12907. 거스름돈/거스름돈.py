def solution(n, money):
    money.sort()
    dp = [1] + [0] * n
    
    for coin in money:
        for i in range(1, n + 1):
            if i - coin >= 0:
                dp[i] += dp[i - coin] 

        
    answer = dp[n]
    return answer