# dfs, bfs 다 가능

import sys
sys.setrecursionlimit(10001)

def solution(maps):
    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
    n, m = len(maps), len(maps[0])
    
    in_range = lambda r, c: 0 <= r < n and 0 <= c < m
    
    def dfs(r, c, visited):
        count = int(maps[r][c])
        visited[r][c] = flag
        
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc):
                continue
            if visited[nr][nc] == flag or maps[nr][nc] == 'X':
                continue
            count += dfs(nr, nc, visited)
            
        return count

    visited = [[0] * m for _ in range(n)]
    flag = 1
    answer = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                total = dfs(i, j, visited)
                answer.append(total)
            
    return sorted(answer) if answer else [-1]
