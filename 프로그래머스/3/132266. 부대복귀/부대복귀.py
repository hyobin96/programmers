import heapq

def solution(n, roads, sources, destination):
    edges = [[] for _ in range(n + 1)]
    for u, v in roads:
        edges[u].append(v)
        edges[v].append(u)
    
    INF = 2e9
    dists = [INF] * (n + 1)
    dists[destination] = 0
    pq = []
    heapq.heappush(pq, (0, destination))
    
    while pq:
        dist, u = heapq.heappop(pq)
        if dist != dists[u]:
            continue
            
        for v in edges[u]:
            new_dist = dists[u] + 1
            if dists[v] > new_dist:
                dists[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
                
    recall_times = []
    for source in sources:
        recall_times.append(dists[source] if dists[source] != INF else -1)
    
    answer = recall_times
    return answer