import heapq

def solution(N, road, K):
    INF = 2e9
    
    edges = [[] for _ in range(N + 1)]
    for u, v, w in road:
        edges[u].append((v, w))
        edges[v].append((u, w))
    
    dists = [INF] * (N + 1)
    dists[1] = 0
    
    pq = []
    heapq.heappush(pq, (0, 1))
    
    while pq:
        w, u = heapq.heappop(pq)
        if dists[u] != w:
            continue
        
        for v, w in edges[u]:
            new_dist = dists[u] + w
            if dists[v] > new_dist:
                dists[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    count = 0
    for i in range(1, N + 1):
        if dists[i] <= K:
            count += 1
            
    answer = count
    return answer