import sys
sys.setrecursionlimit(100_000)

def solution(n, lighthouse):
    tree = [[] for _ in range(n + 1)]
    for u, v in lighthouse:
        tree[u].append(v)
        tree[v].append(u)
    
    dp = [[0] * 2 for _ in range(n + 1)]
    
    def dfs(curr, prev, tree, dp):
        dp[curr][1] = 1
        
        for nxt in tree[curr]:
            if nxt == prev:
                continue
            dfs(nxt, curr, tree, dp)
            dp[curr][1] += min(dp[nxt])
            dp[curr][0] += dp[nxt][1]
            
    dfs(1, 0, tree, dp)
        
    answer = min(dp[1])
    return answer