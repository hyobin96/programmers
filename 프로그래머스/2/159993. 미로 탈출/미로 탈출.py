# bfs 두 번
# (큐, 출발, 도착)

from collections import deque

def solution(maps):
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    n, m = len(maps), len(maps[0])
    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
    in_range = lambda r, c: 0 <= r < n and 0 <= c < m
    
    def bfs(q, end, visited):
        while q:
            r, c, s = q.popleft()
            if maps[r][c] == end:
                return s
            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc):
                    continue
                if visited[nr][nc] == visit_flag or maps[nr][nc] == 'X':
                    continue
                visited[nr][nc] = visit_flag
                q.append((nr, nc, s + 1))
        return -1
    
    start, lever = 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j, 0)
            if maps[i][j] == 'L':
                lever = (i, j, 0)
    
    visited = [[0] * m for _ in range(n)]
    visit_flag = 1
    
    q = deque()
    q.append(start)
    S_to_L = bfs(q, 'L', visited)
    
    visit_flag = 2
    q = deque()
    q.append(lever)
    L_to_E = bfs(q, 'E', visited)
    
    answer = -1
    if S_to_L != -1 and L_to_E != -1:
        answer = S_to_L + L_to_E
        
    return answer