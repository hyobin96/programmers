# n ** 3
# 각 지역에 합승한 후 각자 구역 가기
# 같은 방향쪽에 있다면?
# 어차피 최소값은 올바르게 측정됨

def solution(n, s, a, b, fares):
    INF = 2e9
    dists = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dists[i][i] = 0
        
    for u, v, w in fares:
        dists[u][v] = min(dists[u][v], w)
        dists[v][u] = min(dists[v][u], w)
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
                
    min_cost = dists[s][a] + dists[s][b]
    for i in range(1, n + 1):
        if i == s: continue
        cost = dists[s][i] + dists[i][a] + dists[i][b]
        min_cost = min(min_cost, cost)
    
    
    answer = min_cost
    return answer