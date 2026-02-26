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
    heapq.heappush(pq, destination)
    
    while pq:
        u = heapq.heappop(pq)
        for v in edges[u]:
            if dists[v] > dists[u] + 1:
                dists[v] = dists[u] + 1
                heapq.heappush(pq, v)
                
    recall_times = []
    for source in sources:
        recall_times.append(dists[source] if dists[source] != INF else -1)
    
    answer = recall_times
    return answer