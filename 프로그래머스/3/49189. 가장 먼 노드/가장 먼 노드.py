from collections import deque

def solution(n, edge):
    edges = [[] for _ in range(n + 1)]
    for u, v in edge:
        edges[u].append(v)
        edges[v].append(u)
        
    q = deque()
    q.append(1)
    size = 0
    visited = [0] * (n + 1)
    visited[1] = 1
    while q:
        size = len(q)
        for _ in range(size):
            u = q.popleft()
            for v in edges[u]:
                if visited[v]:
                    continue
                visited[v] = 1
                q.append(v)
        
    answer = size
    return answer