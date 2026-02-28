# 좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y
# 다 1로 표현?
# 선을 표현하기 어려움
# 스케일을 2배로?

def solution(rectangle, characterX, characterY, itemX, itemY):
    def draw_rectangle(rectangle, board):
        x1, y1, x2, y2 = rectangle
        for i in range(y1 * 2, y2 * 2 + 1):
            for j in range(x1 * 2, x2 * 2 + 1):
                board[i][j] = 1
        
    def clear_rectangle(rectangle, board):
        x1, y1, x2, y2 = rectangle
        for i in range(y1 * 2 + 1, y2 * 2):
            for j in range(x1* 2 + 1, x2 * 2):
                board[i][j] = 0
        
    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)

    
    board = [[0] * 104 for _ in range(104)]
    for rect in rectangle:
        draw_rectangle(rect, board)
    
    for rect in rectangle:
        clear_rectangle(rect, board)    
    # for r in range(18, 0, -1):
    #     print(board[r][1:18])
        
    
    in_range = lambda r, c: 1 <= r <= 104 and 1 <= c <= 104
    def dfs(cX, cY, dist):
        nonlocal min_dist, visited
        if cX == itemX * 2 and cY == itemY * 2:
            min_dist = min(min_dist, dist)
            return
        
        visited[cY][cX] = 1
        
        for dr, dc in zip(drs, dcs):
            nr, nc = cY + dr, cX + dc
            if board[nr][nc] and not visited[nr][nc]:
                dfs(nc, nr, dist + 1)
                
                
            
    min_dist = 2e9
    visited = [[0] * 105 for _ in range(105)]
    dfs(characterX * 2, characterY * 2, 0)
    
    answer = min_dist // 2
    return answer