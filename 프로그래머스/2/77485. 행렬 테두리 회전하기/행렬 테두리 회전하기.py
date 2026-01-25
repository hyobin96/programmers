# 시작 행렬 채우기
# 회전하기 -> 기존걸 복사해두고 거기서 가져오기
# 2 2 5 4 -> i = 2 -> 5 , j = 2 -> 4
# i 고정 j 이동, j 고정 i 이동,
# 이동하면서 복사해둔거에서 가져오기
# 반복

def solution(rows, columns, queries):
    def copy_grid(x1, y1, x2, y2):
        copied_grid = []
        for j in range(y1, y2 + 1):
            copied_grid.append(grid[x1][j])
        for i in range(x1 + 1, x2 + 1):
            copied_grid.append(grid[i][y2])
        for j in range(y2 - 1, y1 - 1, -1):
            copied_grid.append(grid[x2][j])
        for i in range(x2 - 1, x1 - 1, -1):
            copied_grid.append(grid[i][y1])
        
        return copied_grid
        
    grid = [[0] * columns for _ in range(rows)]
    
    num = 1
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = num
            num += 1
    
    answer = []        
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        copied_grid = copy_grid(x1, y1, x2, y2)
        answer.append(min(copied_grid))
        idx = 0
        for j in range(y1 + 1, y2 + 1):
            grid[x1][j] = copied_grid[idx]
            idx += 1
        for i in range(x1 + 1, x2 + 1):
            grid[i][y2] = copied_grid[idx]
            idx += 1
        for j in range(y2 - 1, y1 - 1, -1):
            grid[x2][j] = copied_grid[idx]
            idx += 1
        for i in range(x2 - 1, x1 - 1, -1):
            grid[i][y1] = copied_grid[idx]
            idx += 1
            
    
    return answer