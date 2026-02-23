def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
        
    problems.sort()

    n, m = max(alp, max_alp), max(cop, max_cop)
    dp = [[1e5] * (m + 1) for _ in range(n + 1)]
    
    if max_alp <= alp and max_cop <= cop:
        return 0
    
    for i in range(alp + 1):
        for j in range(cop + 1):
            if i <= n and j <= m:
                dp[i][j] = 0
        
    for i in range(min(max_alp, alp), n + 1):
        for j in range(m + 1):
            if dp[i][j] == 1e6:
                continue
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req: 
                    ni = alp_rwd + i if alp_rwd + i <= n else max_alp
                    nj = cop_rwd + j if cop_rwd + j <= m else max_cop
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + cost)
                elif i < alp_req:
                    break
            if i + 1 <= n:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= m:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
        
    min_cost = dp[max_alp][max_cop]
    # for i in range(alp, max_alp + 1):
    #     print(dp[i][cop:])
    answer = min_cost
    return answer