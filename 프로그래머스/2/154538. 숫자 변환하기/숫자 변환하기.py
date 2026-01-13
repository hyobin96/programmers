# dp[i]는 i가 될 수 있는 최소 연산 횟수
#

def solution(x, y, n):
    dp = [2e9] * (y + 1)
    dp[x] = 0
    
    for i in range(x, y):
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)   
    
    return dp[y] if dp[y] != 2e9 else -1