# 방문한 곳은 장애물, 가장자리에 갔을 때
# bfs로 하면 최소를 보장하지 못할 듯 ? 할 듯? 할 듯.
# 왔던 곳으로는 가면 무한반복
# 왔던 방향을 기억해야 함.
# [온 방향, r, c, 움직임 횟수]

from collections import deque

def solution(board):
    n, m = len(board), len(board[0])  # 행, 열
    # 상 좌 하 우, + 2 하면 반대방향
    drs, dcs = (-1, 0, 1, 0), (0, -1, 0, 1)
    
    in_range = lambda r, c: 0 <= r < n and 0 <= c < m
    
    def go_straight(direction, r, c):
        dr, dc = drs[direction], dcs[direction]
        while True:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc):
                return r, c
            if board[nr][nc] == 'D':
                return r, c
            r, c = nr, nc
            
    R, G = 0, 0
            
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                R = (i, j)
            if board[i][j] == 'G':
                G = (i, j)
    
    q = deque()
    visited = [[0] * m for _ in range(n)]
    
    for i in range(4):
        dr, dc = drs[i], dcs[i]
        nr, nc = R[0] + dr, R[1] + dc
        if in_range(nr, nc) and board[nr][nc] != 'D':
            q.append((i, R[0], R[1], 0))
        else:
            visited[R[0]][R[1]] = 1
            
    # print(q)
    answer = -1
    while q:
        direction, r, c, count = q.popleft()
        # print(direction, r, c, count)
        for i in range(4):
            if i == (direction + 2) % 4: # 왔던쪽으로는 안가게
                continue

            nr, nc = go_straight(i, r, c)
            if (nr, nc) == (G[0], G[1]):
                answer = count + 1
                return answer
            
            if visited[nr][nc]:
                continue
            q.append((i, nr, nc, count + 1))
            visited[nr][nc] = 1
            
            
        
    return answer